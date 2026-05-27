# aigames — Servidor Web 🌐

Permite jugar a los juegos de `aigames` directamente desde el navegador usando un servidor local.

## Requisitos

- Python 3.7 o superior
- Sistema Unix/Linux/macOS (se usa `pty` para la terminal — **no funciona en Windows**)

## Instalación

```bash
cd web
pip install -r requirements.txt
```

## Ejecutar el servidor

```bash
python3 app.py
```

Abre `http://localhost:5000` en tu navegador y elige un juego.

## Variables de entorno

| Variable | Descripción | Default |
|----------|-------------|---------|
| `PORT`   | Puerto del servidor | `5000` |
| `SECRET_KEY` | Clave de sesión de Flask | aleatoria por arranque |

Ejemplo con puerto personalizado:

```bash
PORT=8080 python3 app.py
```

## Cómo funciona

1. **Backend:** Flask + Socket.IO gestiona las conexiones WebSocket.
2. **PTY:** Al iniciar un juego, el servidor crea una pseudo-terminal (`pty`) que ejecuta el script Python correspondiente.
3. **Frontend:** [xterm.js](https://xtermjs.org/) renderiza la salida del juego como una terminal real en el navegador y reenvía las pulsaciones de teclas al proceso Python.
4. Al cerrar la conexión, el proceso del juego se termina automáticamente.

## Funciones añadidas

- Filtro por texto, género y dificultad en la portada.
- Botón de juego aleatorio para descubrir títulos rápido.
- Endpoint `GET /api/games` con el catálogo completo en JSON.
- Manejo de sesión más robusto para evitar procesos huérfanos al terminar una partida.

## GitHub Pages

El repositorio también publica un escaparate estático en `docs/` mediante GitHub Pages, pero:

- **sí** sirve para presentar el catálogo y enlazar al código
- **no** puede ejecutar la app Flask ni los juegos interactivos

## Estructura

```
web/
├── app.py              # Servidor Flask + Socket.IO
├── requirements.txt    # Dependencias Python
├── README.md           # Este archivo
└── templates/
    ├── index.html      # Página de inicio con lista de juegos
    └── play.html       # Página de juego con terminal xterm.js
```

## Notas de seguridad

- El servidor solo está pensado para uso local o en redes de confianza.
- Cada cliente recibe su propio proceso aislado del juego.
- Los procesos de juego se terminan automáticamente al desconectarse el navegador.
- No exponer en internet sin añadir autenticación y rate limiting.
