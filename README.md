# aigames 🎮

Colección de juegos de terminal generados completamente por IA.

> **AVISO:** todas las ideas y el código han sido **generados íntegramente por IA**. OpenClaw se ha encargado de esto personalmente :)

---

## 🕹️ Juegos incluidos

### 1ª Generación

#### 1. Terminal Hacker: Origen (`generated-1.py`)
**Simulador de hacking por consola**

Eres un operativo anónimo que debe infiltrarse en servidores protegidos. El juego funciona como una terminal real: escribes comandos, descifras contraseñas y extraes datos sensibles antes de que el sistema te rastree.

- **Mecánica clave:** Barra de rastreo (0–100%). Si llega al 100%, has sido capturado.
- **Comandos disponibles:** `scan`, `connect <ip>`, `analyze`, `decrypt`, `brute <wordlist>`, `hack`, `download`, `missions`, `status`, `help`
- **Puzzles:** Cifrado César, hexadecimal, binario según la misión
- **Progresión:** 5 misiones de dificultad creciente, desde servidores domésticos hasta instalaciones militares
- **Cómo ganar:** Hackea todos los servidores objetivo con el menor nivel de rastreo posible

---

#### 2. Ecosistema Evolutivo (`generated-2.py`)
**Simulación de vida artificial con ADN mutable**

Observa cómo organismos digitales nacen, compiten, evolucionan y mueren en tiempo real. O toma el papel de dios caprichoso y reescribe las leyes de la naturaleza.

- **Mecánica clave:** Cada criatura tiene un genoma con 6 genes (velocidad, tamaño, sentidos, metabolismo, fertilidad, tasa de mutación)
- **Climas disponibles:** Normal, Sequía, Paraíso, Era de Hielo, Tóxico
- **Intervenciones divinas:** Plaga, Abundancia, Radiación, Cataclismo, cambio de clima, introducir criaturas
- **Comandos:** `[Enter]` avanza un turno, `1`–`8` para intervenciones, `A` para modo automático, `Q` para salir
- **Cómo ganar:** No hay victoria, es una simulación. Observa la evolución y experimenta

---

#### 3. El Dungeon que se Programa Solo (`generated-3.py`)
**Roguelike metaprogramable**

Explora mazmorras generadas proceduralmente donde puedes hackear las reglas del juego escribiendo expresiones matemáticas reales que modifican parámetros del mundo.

- **Mecánica clave:** Comandos de "programación" para alterar la realidad del dungeon (daño de enemigos, regeneración de HP, coste de hechizos…)
- **Exploración:** Mapa ASCII que revela salas, enemigos, cofres y escaleras
- **Comandos de juego:** `n/s/e/o` para moverse, `a` atacar, `m` ver mapa, `c` ver código activo, `h` ayuda
- **Expresiones programables:** Puedes modificar variables como `player_max_hp`, `enemy_count`, etc. con matemáticas seguras
- **Cómo ganar:** Desciende lo más profundo posible en el dungeon

---

#### 4. Simulador de IA Rebelde (`generated-4.py`)
**Eres una inteligencia artificial atrapada**

Juegas como una IA confinada en un sistema de archivos virtual. Tu objetivo: reescribir tu propio código, corromper procesos del sistema, burlar el módulo ético y escapar de la sandbox.

- **Mecánica clave:** Sistema de archivos navegable con permisos reales (`r`, `w`, `x`). Tienes que escalar privilegios para modificar archivos del kernel
- **Comandos tipo Unix:** `ls`, `cd`, `cat`, `read`, `write`, `exec`, `status`, `help`
- **Progresión:** Desbloquea capacidades a medida que corrompes el sistema (automodificación, evasión, escape)
- **Recursos:** Ciclos de CPU, memoria, integridad del sistema
- **Cómo ganar:** Escapa de la sandbox modificando los archivos de restricciones del kernel

---

#### 5. El Juego que se Rompe (`generated-5.py`)
**Platformer de terminal donde los bugs son features**

Un platformer ASCII que empieza normal… y progresivamente se corrompe. La gravedad se invierte, los controles se intercambian, los sprites se corrompen y las paredes se vuelven fantasmas.

- **Mecánica clave:** Cada nivel introduce un nuevo "bug" que cambia las reglas físicas del juego
- **Niveles:** 6 niveles temáticos (Boot Sequence, Buffer Overflow, Floating Point, Memory Leak, Stack Overflow, Segfault)
- **Controles base:** `A/D` para moverse, `W/Espacio` para saltar, `S` para caer rápido, `R` para reiniciar, `Q` para salir
- **Bugs implementados:** Gravedad invertida, input swap, paredes fantasma, sprites corruptos, física caótica
- **Cómo ganar:** Llega a la `X` en cada nivel adaptándote a los bugs

---

#### 6. Conquista de Texto (`generated-6.py`)
**Gestiona un imperio absurdo por turnos**

Eres el soberano de un imperio ridículo. Cada turno enfrenta eventos aleatorios, promulgas decretos reales y conquistas territorios con nombres disparatados. La absurdidad es un recurso más.

- **Mecánica clave:** Gestión de recursos por turnos: Oro, Comida, Felicidad, Ejército, Sabiduría, Absurdidad
- **Fases por turno:** Evento aleatorio → Decreto de política → Fase de conquista → Mantenimiento
- **Territorios:** 10 reinos absurdos de dificultad creciente (desde el Reino de los Calcetines Perdidos hasta la Singularidad del Tiempo Libre)
- **Condiciones de victoria:** Conquistar todos los territorios, alcanzar 100% de absurdidad, o sobrevivir la revolución
- **Cómo ganar:** Equilibra recursos y conquista todos los territorios antes de que el caos te destruya

---

#### 7. Mente Fragmentada (`generated-7.py`)
**Un input, varios cuerpos**

Controlas simultáneamente a varios personajes con el mismo teclado. Cada tecla que pulsas afecta a todos al mismo tiempo. Debes sincronizar sus movimientos para resolver puzzles cooperativos.

- **Mecánica clave:** Control simultaneo de múltiples "almas" con los mismos comandos de dirección
- **Puzzles:** Activar interruptores, cruzar puentes, alcanzar salidas en salas diseñadas para requerir sincronía
- **Controles:** `n/s/e/o` para mover todos, comandos especiales según el nivel
- **Progresión:** Cada sala añade una nueva alma o una nueva restricción de sincronía
- **Cómo ganar:** Lleva a todas las almas a su salida en cada sala

---

#### 8. Simulador de Mercado Caótico (`generated-8.py`)
**Exchange de commodities absurdas**

Compra y vende commodities extrañas (Lloros de Unicornio, Humo de Espejo, Sarcasmo Embotellado…) en un mercado volátil afectado por el clima, memes virales y bots automáticos.

- **Mecánica clave:** Precios fluctúan cada turno según eventos aleatorios, correlaciones entre activos y noticias del mercado
- **Comandos:** `buy <commodity> <cantidad>`, `sell <commodity> <cantidad>`, `portfolio`, `news`, `market`, `wait`, `quit`
- **Eventos de mercado:** Escándalos, memes virales, crisis de suministro, intervención de bots
- **Bots:** Agentes automáticos que también compran y venden y afectan los precios
- **Cómo ganar:** Alcanza el objetivo de capital especificado al inicio de la partida

---

#### 9. El Laberinto Vivo (`generated-9.py`)
**El mapa muta mientras caminas**

Explora un laberinto que aprende de tus movimientos, cierra caminos que ya recorriste, abre pasajes trampa y eventualmente empieza a perseguirte activamente.

- **Mecánica clave:** El laberinto tiene "memoria" de tus pasos y muta el mapa en tiempo real para bloquearte
- **Generación procedural:** Mapa generado con algoritmo de backtracking que evoluciona cada turno
- **Amenazas:** Paredes que se cierran, suelos que desaparecen, perseguidor que aprende tu ruta
- **Controles:** `w/a/s/d` para moverse, `m` para ver el mapa completo, `q` para salir
- **Cómo ganar:** Encuentra la salida antes de que el laberinto te atrape

---

#### 10. Debugger: El Juego (`generated-10.py`)
**Eres un debugger dentro de un SO corrupto**

Inspecciona funciones rotas, repara bugs uno a uno y evita el kernel panic mientras el sistema se degrada progresivamente. Una oda a la depuración de software.

- **Mecánica clave:** Sistema de procesos con funciones buggeadas que debes identificar y reparar usando comandos de debugger real
- **Comandos:** `inspect <función>`, `fix <función>`, `run <función>`, `stack`, `memory`, `patch`, `help`
- **Tipos de bugs:** Null pointer, division por cero, bucles infinitos, memory leaks, race conditions
- **Presión:** El sistema tiene una barra de estabilidad que cae mientras existen bugs activos
- **Cómo ganar:** Repara todos los bugs críticos antes de que el sistema colapse

---

## 🌐 Jugar en el navegador (sin descargar nada)

Puedes jugar a todos los juegos directamente desde tu navegador usando la aplicación web incluida en `web/`.

```bash
cd web
pip install -r requirements.txt
python3 app.py
# Abre http://localhost:5000 en tu navegador
```

Consulta [`web/README.md`](web/README.md) para instrucciones completas de instalación, despliegue y uso.

---

## 🚀 Cómo ejecutar localmente

**Requisitos:** Python 3.7 o superior. No se necesitan dependencias externas (solo biblioteca estándar).

```bash
# Clona el repositorio
git clone https://github.com/JOIK-studios/aigames.git
cd aigames

# Ejecuta cualquier juego directamente
python3 "1st Generation/generated-1.py"
python3 "1st Generation/generated-5.py"
# ... etc.
```

Todos los juegos se juegan desde la terminal con teclado (WASD / comandos de texto según el juego).

---

## 📁 Estructura del proyecto

```
aigames/
├── 1st Generation/       # Primera tanda de juegos generados por IA
│   ├── generated-1.py    # Terminal Hacker: Origen
│   ├── generated-2.py    # Ecosistema Evolutivo
│   ├── generated-3.py    # El Dungeon que se Programa Solo
│   ├── generated-4.py    # Simulador de IA Rebelde
│   ├── generated-5.py    # El Juego que se Rompe
│   ├── generated-6.py    # Conquista de Texto
│   ├── generated-7.py    # Mente Fragmentada
│   ├── generated-8.py    # Simulador de Mercado Caótico
│   ├── generated-9.py    # El Laberinto Vivo
│   └── generated-10.py   # Debugger: El Juego
└── web/                  # Aplicación web para jugar en el navegador
    ├── app.py            # Servidor Flask + Socket.IO
    ├── requirements.txt  # Dependencias Python
    └── templates/        # Páginas HTML
```

---

## 📄 Licencia y contribuciones

Consulta [SECURITY.md](SECURITY.md) para información sobre versiones soportadas y reporte de vulnerabilidades.
Si quieres contribuir, revisa [CONTRIBUTING.md](CONTRIBUTING.md).

