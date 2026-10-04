# Banxico — Cubo de Comercio Exterior

- Consulta: 3 oct 2026
- Página oficial abierta: https://www.banxico.org.mx/CuboComercioExterior/
- Visores abiertos el mismo día:
  - https://www.banxico.org.mx/CuboComercioExterior/ValorDolares/inicio
  - https://www.banxico.org.mx/CuboComercioExterior/ValorDolaresAnual/inicio
  - https://www.banxico.org.mx/CuboComercioExterior/ValorDolares/seriesproducto
- Forma: software de consulta (embebe `https://tablero.banxico.org.mx/no-shell/embed.js`, Pyramid Analytics, storyboard `3b425ee8-aa7e-4e28-a63e-29f5c253d3fd`). No hay ZIP ni CSV completo en esas páginas.
- Unidad que declara la página de bienvenida: valor en dólares (tratamiento estadístico). Volumen solo a nivel fracción, sin tratamiento estadístico.
- El tutorial usa desde enero 1993. Las páginas abiertas no publican la fecha final.

## Exportación

La ayuda en la misma página: clic derecho → copiar datos, o Imprimir → Excel. Si la consulta cabe en más celdas que el máximo de filas de Microsoft Office, Excel trunca. La cantidad copiada al portapapeles depende del navegador. Las gráficas no se exportan.

Sondeo el mismo día: esas URLs no enlazan un `.csv` ni un `.zip`. `https://tablero.banxico.org.mx/` y `/no-shell/` respondieron HTTP 401. `/ValorDolares/export` y `/ValorDolares/csv` respondieron 404. La SIE API (`/SieAPIRest/service/v1/`) no es este cubo.

No se publica un CSV. Un recorte truncado de Excel no es el cubo.

## No mezclar

Preliminar; puede no coincidir con la BCMM de INEGI. No se junta con los ZIP mensuales de capítulo ni de país ni con el extracto OLAP.
