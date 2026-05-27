# Contribuir a aigames

## Alcance

Este repositorio mezcla juegos de terminal y una app web local para lanzarlos desde el navegador.

## Cambios recomendados

- Mantén los cambios pequeños y enfocados.
- Evita modificar varios juegos a la vez si no es necesario.
- Si tocas `web/`, valida que el servidor siga arrancando y que el código Python compile.
- Si actualizas documentación, asegúrate de que las rutas y comandos sigan siendo correctos.

## Validación mínima

```bash
python3 -m compileall "1st Generation" web
```

## Seguridad

- No expongas la app web en internet sin autenticación y limitación de tráfico.
- No añadas secretos al repositorio.
