# INEGI OLAP — capítulo × país × fracción

- Consulta: 3 oct 2026
- Página oficial abierta: https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/comex/comex_bcmm_mensual2023.asp
- Cubo hermano abierto el mismo día (no extraído): https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/comex/comex_bcmm_mensual2021_2022.asp
- Forma: consulta OLAP + `exporta.aspx` CSV. No es ZIP oficial.
- Cubo: `COMEX_BCMM_MENSUAL` / `COMEX_BCMM_MENSUAL_2023`
- Cobertura que declara la página: enero 2023 – julio 2026
- Unidad que declara la página: dólares FOB y cantidad (UMED de la TIGIE)
- TIGIE 12 dic 2022, SA 2022. Definitivas 2023 y 2024; desde 2025, revisadas. «C» = confidencial.

## Qué se pidió

El cruce completo capítulo × país × fracción, no un capítulo de muestra.

## Qué se obtuvo

43 CSV oficiales, uno por mes, en `datos/olap_bcmm_mensual2023/`. Cada archivo es la exportación del visor (`Texto separado por comas`) de:

`Tipo operación.Children × País.Children × Descendants(Tarifa.Total, 4)`

con filtro de año, mes y US dólares. La fracción de 8 dígitos lleva el capítulo en los dos primeros dígitos.

Cada mes se publicó solo cuando el número de filas `Importaciones`/`Exportaciones` del CSV fue igual a `Cant_Fil` de `Actualiza`. En julio 2026: 107 424 filas = `Cant_Fil`. En febrero 2024 el primer `exporta.aspx` devolvió HTML (82 361 B) con `Cant_Fil` 104 105; el reintento del mismo día coincidió (104 105 filas) y ese CSV sí se publicó.

Suma de filas de los 43 meses: 4 540 560. Ningún archivo llega a 100 MB (el mayor es 11 094 783 B).

## Unidades

Dólares FOB. No se junta con el mensual de capítulo (millones) ni con el mensual de país (miles).
