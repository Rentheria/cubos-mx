# Banxico — Cubo de Comercio Exterior

Consulta 4 oct 2026, 02:06 UTC. Banxico no entrega un CSV/ZIP del cubo completo. SIDIE (`dataset?ruta=Cubo`) responde 200 con el texto «Todavía no existe ningún registro.» `tablero.banxico.org.mx` responde HTTP 401 (`YOU DON'T HAVE THE AUTHORIZATION`). Las rutas tipo `/datos.csv` y `/cubo.zip` responden 404 (103 B).

No hay archivo de datos aquí. Un Excel truncado no es el cubo. No se publican los ZIP de SIDIE MLL (mercados laborales) como si fueran este cubo.

Registro HTTP: [probe.json](probe.json). Nota: [../extractos/BANXICO_cubo.md](../extractos/BANXICO_cubo.md).
