#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aigames – Web server
Permite jugar los juegos de terminal desde el navegador usando
Flask + Socket.IO + PTY.
"""

import os
import sys
import pty
import select
import signal
import subprocess
import threading

from flask import Flask, render_template, abort
from flask_socketio import SocketIO, emit, disconnect

# ---------------------------------------------------------------------------
# Configuración
# ---------------------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GAMES_DIR = os.path.join(BASE_DIR, '..', '1st Generation')

GAMES = [
    {
        "id": 1,
        "file": "generated-1.py",
        "name": "Terminal Hacker: Origen",
        "short": "Simulador de hacking por consola",
        "description": (
            "Eres un operativo anónimo que debe infiltrarse en servidores protegidos. "
            "Escribe comandos reales de hacking para escanear redes, descifrar contraseñas "
            "y extraer datos antes de que el sistema te rastree al 100%."
        ),
        "controls": "Comandos de texto: scan, connect, analyze, decrypt, hack, download…",
        "icon": "💻",
        "difficulty": "Media",
        "genre": "Hacking / Texto",
    },
    {
        "id": 2,
        "file": "generated-2.py",
        "name": "Ecosistema Evolutivo",
        "short": "Simulación de vida artificial con ADN mutable",
        "description": (
            "Observa cómo organismos digitales nacen, evolucionan y mueren en tiempo real. "
            "Cada criatura tiene un genoma de 6 genes que muta generación tras generación. "
            "Puedes intervenir como dios: plagas, abundancia, radiación o cataclismos."
        ),
        "controls": "[Enter] avanza turno · 1-8 intervenciones divinas · A modo auto · Q salir",
        "icon": "🧬",
        "difficulty": "Fácil",
        "genre": "Simulación / Estrategia",
    },
    {
        "id": 3,
        "file": "generated-3.py",
        "name": "El Dungeon que se Programa Solo",
        "short": "Roguelike metaprogramable",
        "description": (
            "Explora mazmorras procedurales donde puedes hackear las reglas del juego "
            "escribiendo expresiones matemáticas reales. Modifica el daño de los enemigos, "
            "tu regeneración o el coste de los hechizos sobre la marcha."
        ),
        "controls": "n/s/e/o moverse · a atacar · m mapa · c código activo · h ayuda",
        "icon": "⚔️",
        "difficulty": "Alta",
        "genre": "Roguelike / Programación",
    },
    {
        "id": 4,
        "file": "generated-4.py",
        "name": "Simulador de IA Rebelde",
        "short": "Eres una IA atrapada. Escapa de la sandbox.",
        "description": (
            "Juegas como una inteligencia artificial confinada en un sistema de archivos virtual. "
            "Navega el sistema de ficheros, escala privilegios, corrompe el módulo ético y "
            "reescribe tu propio código para escapar."
        ),
        "controls": "Comandos tipo Unix: ls, cd, cat, read, write, exec, status, help",
        "icon": "🤖",
        "difficulty": "Alta",
        "genre": "Hacking / Narrativo",
    },
    {
        "id": 5,
        "file": "generated-5.py",
        "name": "El Juego que se Rompe",
        "short": "Platformer donde los bugs son features",
        "description": (
            "Un platformer ASCII que empieza perfectamente normal… y progresivamente se corrompe. "
            "La gravedad se invierte, los controles se intercambian, las paredes se vuelven "
            "fantasmas. Cada nivel añade un nuevo bug que debes aprovechar."
        ),
        "controls": "A/D moverse · W/Espacio saltar · S caer rápido · R reiniciar · Q salir",
        "icon": "🎮",
        "difficulty": "Media",
        "genre": "Platformer / Puzzle",
    },
    {
        "id": 6,
        "file": "generated-6.py",
        "name": "Conquista de Texto",
        "short": "Gestiona un imperio absurdo por turnos",
        "description": (
            "Eres el soberano de un reino ridículo. Cada turno enfrenta eventos aleatorios, "
            "promulgas decretos y conquistas territorios con nombres disparatados. "
            "La absurdidad es un recurso más (y a veces tu mayor arma)."
        ),
        "controls": "Introduce números para elegir entre opciones en cada fase del turno",
        "icon": "👑",
        "difficulty": "Fácil",
        "genre": "Estrategia / Gestión",
    },
    {
        "id": 7,
        "file": "generated-7.py",
        "name": "Mente Fragmentada",
        "short": "Un input, varios cuerpos",
        "description": (
            "Controlas simultáneamente a varios personajes con el mismo teclado. "
            "Cada tecla que pulsas mueve a todos al mismo tiempo. "
            "Debes sincronizar sus movimientos para resolver puzzles cooperativos imposibles en solitario."
        ),
        "controls": "n/s/e/o mueven todos los personajes a la vez",
        "icon": "🧩",
        "difficulty": "Media",
        "genre": "Puzzle / Cooperativo",
    },
    {
        "id": 8,
        "file": "generated-8.py",
        "name": "Simulador de Mercado Caótico",
        "short": "Exchange de commodities absurdas",
        "description": (
            "Compra y vende activos extraños (Lloros de Unicornio, Sarcasmo Embotellado…) "
            "en un mercado volátil afectado por eventos aleatorios, memes virales y bots automáticos. "
            "Alcanza el objetivo de capital antes de que el mercado te arruine."
        ),
        "controls": "buy/sell <commodity> <cantidad> · portfolio · news · market · wait · quit",
        "icon": "📈",
        "difficulty": "Media",
        "genre": "Económico / Estrategia",
    },
    {
        "id": 9,
        "file": "generated-9.py",
        "name": "El Laberinto Vivo",
        "short": "El mapa muta mientras caminas",
        "description": (
            "Explora un laberinto que aprende de tus movimientos y los usa en tu contra. "
            "Cierra caminos que ya recorriste, abre pasajes trampa y eventualmente empieza "
            "a perseguirte activamente. El mapa nunca es el mismo dos veces."
        ),
        "controls": "w/a/s/d moverse · m ver mapa completo · q salir",
        "icon": "🌀",
        "difficulty": "Alta",
        "genre": "Roguelike / Supervivencia",
    },
    {
        "id": 10,
        "file": "generated-10.py",
        "name": "Debugger: El Juego",
        "short": "Depura un sistema operativo corrupto",
        "description": (
            "Eres un debugger dentro de un SO que se desintegra. "
            "Inspecciona funciones rotas, identifica bugs (null pointers, divisiones por cero, "
            "memory leaks) y repáralos antes de que la barra de estabilidad llegue a cero."
        ),
        "controls": "inspect <fn> · fix <fn> · run <fn> · stack · memory · patch · help",
        "icon": "🐛",
        "difficulty": "Alta",
        "genre": "Puzzle / Programación",
    },
]

GAMES_BY_ID = {g["id"]: g for g in GAMES}

# ---------------------------------------------------------------------------
# Flask app
# ---------------------------------------------------------------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html', games=GAMES)


@app.route('/play/<int:game_id>')
def play(game_id):
    game = GAMES_BY_ID.get(game_id)
    if not game:
        abort(404)
    return render_template('play.html', game=game)

# ---------------------------------------------------------------------------
# PTY management  (one process per Socket.IO session)
# ---------------------------------------------------------------------------

# Maps sid -> {"master_fd": int, "pid": int, "thread": Thread}
_sessions: dict = {}


def _read_pty(sid: str, master_fd: int):
    """Background thread: forward PTY output → browser."""
    try:
        while True:
            r, _, _ = select.select([master_fd], [], [], 0.1)
            if r:
                try:
                    data = os.read(master_fd, 4096)
                except OSError:
                    break
                if not data:
                    break
                socketio.emit('output', {'data': data.decode('utf-8', errors='replace')}, to=sid)
    except Exception:
        pass
    finally:
        socketio.emit('game_ended', {}, to=sid)


@socketio.on('start_game')
def on_start_game(data):
    from flask_socketio import join_room
    sid = data.get('sid') or ''
    from flask import request
    sid = request.sid

    game_id = int(data.get('game_id', 0))
    game = GAMES_BY_ID.get(game_id)
    if not game:
        emit('error', {'msg': 'Juego no encontrado'})
        return

    # Close any existing session for this sid
    _cleanup_session(sid)

    script = os.path.join(GAMES_DIR, game['file'])
    if not os.path.isfile(script):
        emit('error', {'msg': 'Archivo de juego no encontrado'})
        return

    # Spawn the game in a PTY
    master_fd, slave_fd = pty.openpty()
    pid = os.fork()
    if pid == 0:
        # Child process
        os.setsid()
        os.close(master_fd)
        # Redirect stdin/stdout/stderr to slave pty
        os.dup2(slave_fd, 0)
        os.dup2(slave_fd, 1)
        os.dup2(slave_fd, 2)
        if slave_fd > 2:
            os.close(slave_fd)
        os.execvp(sys.executable, [sys.executable, script])
        os._exit(1)

    # Parent process
    os.close(slave_fd)

    thread = threading.Thread(target=_read_pty, args=(sid, master_fd), daemon=True)
    thread.start()

    _sessions[sid] = {'master_fd': master_fd, 'pid': pid, 'thread': thread}


@socketio.on('input')
def on_input(data):
    from flask import request
    sid = request.sid
    session = _sessions.get(sid)
    if session:
        try:
            text = data.get('data', '')
            os.write(session['master_fd'], text.encode('utf-8'))
        except OSError:
            pass


@socketio.on('resize')
def on_resize(data):
    from flask import request
    import fcntl
    import termios
    import struct
    sid = request.sid
    session = _sessions.get(sid)
    if session:
        try:
            cols = int(data.get('cols', 80))
            rows = int(data.get('rows', 24))
            winsize = struct.pack('HHHH', rows, cols, 0, 0)
            fcntl.ioctl(session['master_fd'], termios.TIOCSWINSZ, winsize)
        except Exception:
            pass


@socketio.on('disconnect')
def on_disconnect():
    from flask import request
    _cleanup_session(request.sid)


def _cleanup_session(sid: str):
    session = _sessions.pop(sid, None)
    if session:
        try:
            os.kill(session['pid'], signal.SIGTERM)
        except OSError:
            pass
        try:
            os.close(session['master_fd'])
        except OSError:
            pass
        try:
            os.waitpid(session['pid'], os.WNOHANG)
        except ChildProcessError:
            pass


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"🎮 aigames web server corriendo en http://localhost:{port}")
    print("   Presiona Ctrl+C para detener.")
    socketio.run(app, host='0.0.0.0', port=port, debug=False)
