# INEGI OLAP — capítulo × país × fracción

- Consulta: 3 oct 2026
- Página oficial abierta: https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/comex/comex_bcmm_mensual2023.asp
- Cubo hermano abierto el mismo día: https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/comex/comex_bcmm_mensual2021_2022.asp
- Forma: consulta OLAP (POST a `/sistemas/olap/consulta/general_ver4/MDXQueryDatos.asp`), no ZIP oficial
- Cubo: `COMEX_BCMM_MENSUAL` / `COMEX_BCMM_MENSUAL_2023`
- Cobertura que declara la página: enero 2023 – julio 2026
- Unidad que declara la página: dólares FOB y cantidad (UMED de la TIGIE)
- TIGIE 12 dic 2022, SA 2022. Definitivas 2023 y 2024; desde 2025, revisadas. «C» = confidencial.

## Qué se pidió

El cruce completo capítulo × país × fracción, no un capítulo de muestra.

## Qué se obtuvo

Se envió la consulta con País y Tarifa (la Tarifa del cubo incluye capítulo, partida, subpartida, fracción y NICO; Fracción Arancelaria y NICO es mutuamente excluyente con Tarifa). El visor contestó HTML de «Consulta interactiva de datos» (65,562 bytes). No es un CSV del cruce. La tabla del visor abre en totales y se recorre por páginas y por drill-down.

No se publica un CSV. Un archivo parcial no es el cubo.

## Unidades

Dólares FOB. No se junta con el mensual de capítulo (millones) ni con el mensual de país (miles).
