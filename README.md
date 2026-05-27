# aigames 🎮

Colección de juegos de terminal generados íntegramente por IA, con modo consola y catálogo web.

> **Aviso:** las ideas y el código de los juegos han sido generados por IA.

---

## ✨ Qué incluye ahora

- 10 juegos de terminal en Python puro
- Aplicación web local con Flask + Socket.IO
- Filtros y selección aleatoria en la portada web
- API simple en `/api/games` para listar el catálogo
- Deploy automático de un escaparate estático con GitHub Pages

---

## 🕹️ Catálogo de juegos

| # | Juego | Tipo | Dificultad |
|---|-------|------|------------|
| 1 | Terminal Hacker: Origen | Hacking / Texto | Media |
| 2 | Ecosistema Evolutivo | Simulación / Estrategia | Fácil |
| 3 | El Dungeon que se Programa Solo | Roguelike / Programación | Alta |
| 4 | Simulador de IA Rebelde | Hacking / Narrativo | Alta |
| 5 | El Juego que se Rompe | Platformer / Puzzle | Media |
| 6 | Conquista de Texto | Estrategia / Gestión | Fácil |
| 7 | Mente Fragmentada | Puzzle / Cooperativo | Media |
| 8 | Simulador de Mercado Caótico | Económico / Estrategia | Media |
| 9 | El Laberinto Vivo | Roguelike / Supervivencia | Alta |
| 10 | Debugger: El Juego | Puzzle / Programación | Alta |

Los scripts están en [`/1st Generation`](./1st%20Generation).

---

## 🚀 Ejecutar en local

### Juegos en terminal

**Requisitos:** Python 3.7 o superior.

```bash
git clone https://github.com/JOIK-studio/aigames.git
cd aigames

python3 "1st Generation/generated-1.py"
python3 "1st Generation/generated-5.py"
```

### Aplicación web local

La app web permite jugar desde el navegador, pero necesita un servidor Python local porque crea una pseudo-terminal por partida.

```bash
cd web
pip install -r requirements.txt
python3 app.py
```

Luego abre `http://localhost:5000`.

Más detalles en [`/web/README.md`](./web/README.md).

---

## 🌍 GitHub Pages

Este repositorio ahora incluye un workflow para publicar un **catálogo estático** en GitHub Pages.

- Archivo: [`.github/workflows/deploy-pages.yml`](./.github/workflows/deploy-pages.yml)
- Contenido publicado: [`/docs/index.html`](./docs/index.html)

> GitHub Pages no puede ejecutar la app Flask/Socket.IO ni los juegos interactivos del servidor.  
> Por eso la página desplegada funciona como escaparate, documentación rápida y punto de entrada al repositorio.

Una vez activado Pages en GitHub, el sitio quedará disponible en la URL estándar del repositorio.

---

## 📁 Estructura

```text
aigames/
├── 1st Generation/         # Juegos de terminal
├── docs/                   # Sitio estático para GitHub Pages
├── web/                    # Servidor web local con Flask + Socket.IO
├── README.md
├── CONTRIBUTING.md
└── SECURITY.md
```

---

## 🤝 Contribuir

Consulta [CONTRIBUTING.md](./CONTRIBUTING.md) para cambios, pruebas y estilo básico del repositorio.

## 🔐 Seguridad

Consulta [SECURITY.md](./SECURITY.md) para versiones soportadas y reporte de vulnerabilidades.
