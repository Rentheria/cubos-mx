# INEGI OLAP — tipo × país × fracción (extracto de cubo)

- Consulta: 3 oct 2026
- Página oficial: https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/comex/comex_bcmm_mensual2023.asp
- Cubo: `COMEX_BCMM_MENSUAL` / `COMEX_BCMM_MENSUAL_2023`
- Forma: extracto de cubo (POST a `MDXQueryDatos.asp` y descarga por `exporta.aspx` en CSV). No es ZIP de datos abiertos.
- Periodo: enero 2023 – julio 2026 (43 meses; la página no nombra agosto 2026)
- Unidad: dólares FOB (y cantidad en UMED de la TIGIE, en la misma fila del CSV oficial)
- Cruce: tipo de operación (importación / exportación) × país × fracción de 8 dígitos. El capítulo es el prefijo de dos dígitos de esa fracción (`Descendants([Tarifa].[Tarifa].[Total], 4)`).
- Completitud: cada mes se escribió solo cuando las filas de datos del CSV coincidieron con `Actualiza Cant_Fil` del visor. Suma de los 43 meses: 4 540 560 filas. Índice: `indice.json`.

No se junta con los ZIP mensuales de capítulo ni de país. No se suman dólares de este extracto con millones ni con miles. «C» es confidencial, no cero: la suma de fracciones no tiene que igualar el total del capítulo.

El cubo hermano 2021–2022 no se extrajo aquí.
