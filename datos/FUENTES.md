# Archivos oficiales de INEGI (BCMM)

Tres ZIP de datos abiertos, bajados de INEGI (no Wayback). Aquí está cada archivo que trae cada ZIP, sin quitar filas ni columnas. El Excel no viene en estos ZIP.

Unidades, tomadas del diccionario de cada paquete:

- Modo de transporte (capítulo y aduana), mensual: `VAL_USD` en millones de dólares FOB
- País y tipo de bien, mensual: `VAL_USD` en miles de dólares FOB
- El anual declara su unidad en su propio diccionario y metadatos

Capítulo y país no se juntan. Millones y miles no se suman. No hay CSV de capítulo por país en estos ZIP; ese cruce está en el cubo:
https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/comex/comex_bcmm_mensual2023.asp

## Mensual, modo de transporte (capítulo y aduana)

- ZIP: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_mensual_mtra_csv.zip
- Programa: https://www.inegi.org.mx/programas/comext/
- Carpeta en este repo: `datos/mensual_mtra/`
- Periodo en las tablas: enero 2012 a julio 2026
- Trae exportación e importación en las mismas tablas

Archivos del ZIP (filas = datos, sin encabezado):

- `conjunto_de_datos/bcmm_mtra_capitulo_mensual_tr_cifra_2012_2026.csv` — 26,752,913 B · 171,850 filas (85,925 exportación y 85,925 importación)
- `conjunto_de_datos/bcmm_mtra_aduana_mensual_tr_cifra_2012_2026.csv` — 1,842,836 B · 14,350 filas (7,175 por flujo)
- `catalogos/tc_mtra.csv` — 92 B · 5 filas
- `catalogos/tc_periodo_mes.csv` — 170 B · 12 filas
- `diccionario_de_datos/diccionario_datos_bcmm_mtra_mensual_2012_2026.csv` — 2,709 B · 10 filas
- `metadatos/metadatos_bcmm_mtra_mensual_2012_2026.txt`
- `modelo_entidad_relacion/modelo_er_bcmm_mtra_mensual_2012_2026.png`

## Mensual, país por tipo de bien

- ZIP: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_mensual_paises_bien_csv.zip
- Programa: https://www.inegi.org.mx/programas/comext/
- Carpeta: `datos/mensual_paises_bien/`
- Periodo: enero 2015 a julio 2026
- INEGI parte la tabla en tres CSV. Cada uno trae exportación e importación. País vacío = total de zona, no un país

Archivos del ZIP (filas = datos, sin encabezado):

- `conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2015_2022.csv` — 27,268,595 B · 148,680 filas
- `conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2023_2025.csv` — 10,114,644 B · 55,728 filas
- `conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2026.csv` — 1,964,317 B · 10,836 filas
- `catalogos/tc_continente.csv` — 92 B · 5 filas
- `catalogos/tc_region.csv` — 375 B · 13 filas
- `catalogos/tc_pais.csv` — 4,645 B · 263 filas
- `catalogos/tc_periodo_mes.csv` — 170 B · 12 filas
- `diccionario_de_datos/diccionario_datos_paises_bien_mensual_2015_2026.csv` — 3,402 B · 12 filas
- `metadatos/metadatos_paises_bien_mensual_2015_2022.txt`
- `metadatos/metadatos_paises_bien_mensual_2023_2025.txt`
- `metadatos/metadatos_paises_bien_mensual_2026.txt`
- `modelo_entidad_relacion/modelo_er_paises_bien_mensual_2015_2026.png`

## Anual

- ZIP: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_anual_csv.zip
- Programa: https://www.inegi.org.mx/programas/comext/
- Carpeta: `datos/anual/`
- Periodo: 2003–2025, un CSV por año
- `VAL_USD` en dólares FOB (no millones ni miles). `VAL_MNX` en pesos. `CANTIDAD` según `UMED` de la TIGIE. No se suman con las tablas mensuales.
- Es tarifa (TIGIE) × país. No se junta con el mensual de capítulo ni con el mensual de país.

Tablas (`conjunto_de_datos/`):

| Archivo | Bytes | Filas | En git |
| --- | ---: | ---: | --- |
| `bcmm_anual_tr_cifra_2003.csv` | 77,615,671 | 477,762 | sí |
| `bcmm_anual_tr_cifra_2004.csv` | 80,306,977 | 494,178 | sí |
| `bcmm_anual_tr_cifra_2005.csv` | 78,683,405 | 499,691 | sí |
| `bcmm_anual_tr_cifra_2006.csv` | 80,132,385 | 508,488 | sí |
| `bcmm_anual_tr_cifra_2007.csv` | 134,471,337 | 850,431 | no (≥100 MB; queda en el workspace) |
| `bcmm_anual_tr_cifra_2008.csv` | 83,818,325 | 531,719 | sí |
| `bcmm_anual_tr_cifra_2009.csv` | 83,074,751 | 527,411 | sí |
| `bcmm_anual_tr_cifra_2010.csv` | 86,067,766 | 546,193 | sí |
| `bcmm_anual_tr_cifra_2011.csv` | 87,270,477 | 553,553 | sí |
| `bcmm_anual_tr_cifra_2012.csv` | 148,298,369 | 937,415 | no (≥100 MB; queda en el workspace) |
| `bcmm_anual_tr_cifra_2013.csv` | 90,978,590 | 576,870 | sí |
| `bcmm_anual_tr_cifra_2014.csv` | 91,819,364 | 582,172 | sí |
| `bcmm_anual_tr_cifra_2015.csv` | 82,592,591 | 586,316 | sí |
| `bcmm_anual_tr_cifra_2016.csv` | 83,968,027 | 595,817 | sí |
| `bcmm_anual_tr_cifra_2017.csv` | 84,573,569 | 600,079 | sí |
| `bcmm_anual_tr_cifra_2018.csv` | 86,476,361 | 613,814 | sí |
| `bcmm_anual_tr_cifra_2019.csv` | 86,449,821 | 613,400 | sí |
| `bcmm_anual_tr_cifra_2020.csv` | 82,921,215 | 588,647 | sí |
| `bcmm_anual_tr_cifra_2021.csv` | 91,097,469 | 632,907 | sí |
| `bcmm_anual_tr_cifra_2022.csv` | 122,775,704 | 850,011 | no (≥100 MB; queda en el workspace) |
| `bcmm_anual_tr_cifra_2023.csv` | 121,778,100 | 842,912 | no (≥100 MB; queda en el workspace) |
| `bcmm_anual_tr_cifra_2024.csv` | 120,315,175 | 832,608 | no (≥100 MB; queda en el workspace) |
| `bcmm_anual_tr_cifra_2025.csv` | 120,346,046 | 832,768 | no (≥100 MB; queda en el workspace) |

También en el ZIP: `catalogos/tc_codigo_pais.csv`, `tc_periodo_mes.csv`, `tc_tigie.csv` (60,660,819 bytes), `tc_unidad_medida.csv`, `diccionario_de_datos/diccionario_datos_bcmm_anual_2003_2025.csv`, metadatos 2003–2025 y `modelo_entidad_relacion/modelo_er_bcmm_anual_2003_2025.png`.
