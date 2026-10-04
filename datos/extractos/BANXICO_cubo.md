# Banxico — Cubo de Comercio Exterior

- Consultas: 3 oct 2026 y 4 oct 2026 (esta VM)
- Página oficial: https://www.banxico.org.mx/CuboComercioExterior/
- Visores abiertos:
  - https://www.banxico.org.mx/CuboComercioExterior/ValorDolares/inicio
  - https://www.banxico.org.mx/CuboComercioExterior/ValorDolaresAnual/inicio
  - https://www.banxico.org.mx/CuboComercioExterior/ValorDolares/seriesproducto
- Forma: tablero Pyramid (embebe `https://tablero.banxico.org.mx/no-shell/embed.js`, storyboard `3b425ee8-aa7e-4e28-a63e-29f5c253d3fd`). No hay ZIP ni CSV completo en esas páginas.
- Unidad que declara la bienvenida: valor en dólares (tratamiento estadístico). Volumen solo a nivel fracción, sin tratamiento estadístico.
- El tutorial usa desde enero 1993. Las páginas abiertas no publican la fecha final.

## Qué bloqueó la descarga completa (4 oct 2026)

Se intentó de nuevo desde esta máquina. Resultado:

- Las páginas del cubo responden 200 y no enlazan ningún `.csv` ni `.zip`.
- `https://tablero.banxico.org.mx/` y `/no-shell/` responden **HTTP 401**.
- `/ValorDolares/export` y `/ValorDolares/csv` responden **404**.
- La SIE API no es este cubo.
- La ayuda del propio sitio solo ofrece copiar al portapapeles o Imprimir → Excel, y avisa que Excel trunca si la consulta pasa el máximo de filas de Office. La página no nombra ese máximo.

No se publica un archivo parcial. No se recorre el tablero capítulo por capítulo. Un Excel cortado no es el cubo.

## No mezclar

Preliminar; puede no coincidir con la BCMM de INEGI. No se junta con los ZIP mensuales de capítulo ni de país ni con el extracto OLAP.
