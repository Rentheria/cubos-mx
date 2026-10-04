# Archivos oficiales y extractos (consulta 3 oct 2026)

Inventario de lo que se abrió en vivo el 3 de octubre de 2026. Cada entrada declara URL oficial, fecha de consulta, unidad, periodo y si es ZIP oficial o extracto de cubo. Las filas de datos se contaron en el CSV extraído (líneas menos el encabezado). No se inventaron conteos. No se mezclan paquetes.

Las páginas de programa de INEGI (`/programas/comext/`, `/programas/exporta_ef/`, `/temas/exportacionesef/`) son cascarones JS. El HTML de COMEXT (3 751 B) no lista como liga visible el ZIP mensual genérico; su `schema.org` solo nombra `bcmm_anual_csv.zip`. La existencia de cada ZIP se comprobó por `Content-Type: application/x-zip-compressed` y firma `PK`. URLs inventadas devolvieron `text/html` de 2 263 B.

No se junta capítulo con país. No se suman millones, miles y dólares. ETEF no se dobla dentro de la BCMM.

## Qué desmintieron las páginas vivas

| Afirmación previa | Qué se vio el 3 oct 2026 |
| --- | --- |
| Solo hay tres ZIP de datos abiertos BCMM | Hay un cuarto ZIP oficial: `conjunto_de_datos_bcmm_mensual_csv.zip` (62 602 B, zip real). |
| No hay mes posterior a julio 2026 | El mensual de agregados trae agosto 2026 (Cifras Oportunas). El ZIP de modo de transporte, el de país y el cubo OLAP mensual 2023 siguen en julio 2026. |
| BCMM datos abiertos trae entidad o municipio | `…/conjunto_de_datos_bcmm_mensual_entidad_csv.zip` y `…/municipio_csv.zip` (y `…/aduana_csv.zip` aparte del paquete mtra) son HTML 2 263 B, no zip. |
| El programa ETEF vive en `/programas/exportacionesef/` | Esa URL abre «Página no encontrada» / «Esta liga ya no existe». El programa vivo es https://www.inegi.org.mx/programas/exporta_ef/ |
| El cruce capítulo × país × fracción no se puede bajar del cubo | El 3 oct 2026 `exporta.aspx` sí entregó CSV por mes. 43 archivos en `datos/olap_bcmm_mensual2023/`; cada uno igualó `Cant_Fil`. |
| El cubo de Banxico tiene CSV completo | 4 oct 2026: SIDIE `dataset?ruta=Cubo` 200 «Todavía no existe ningún registro.» Tablero 401. `/datos.csv` y `/cubo.zip` 404 (103 B). Sin dump. |
| El BIE abre | https://www.inegi.org.mx/sistemas/bie/ respondió HTTP 500. |

## BCMM — mensual, agregados (ZIP oficial)

- ZIP extraído en este repo: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_mensual_csv.zip
- Sondeo 3 oct 2026: `application/x-zip-compressed` · 62 602 B · firma `PK`
- Programa: https://www.inegi.org.mx/programas/comext/ (HTML 3 751 B; `schema.org` no nombra este ZIP)
- Carpeta: `datos/mensual/`
- Forma: ZIP oficial (no extracto de cubo)
- Periodo en las tablas extraídas: enero 2012 a agosto 2026. Metadato 2026: «cifras oportunas al mes de agosto»; `modified: 2026-09-28T06:00`; `temporal: 2026-01-01-2026-08-31`
- Unidad (diccionario del paquete): `VAL_USD` en millones de dólares FOB
- Cobertura: nacional. Exportación, importación y saldos en las mismas tablas. Grandes agregados en `CONCEPTO`. No es capítulo, no es país, no es aduana.

Archivos del ZIP (filas = datos, sin encabezado):

- `conjunto_de_datos/bcmm_mensual_tr_cifra_2012_2022.csv` — 312 123 B · 2 376 filas · ene 2012–dic 2022
- `conjunto_de_datos/bcmm_mensual_tr_cifra_2023_2025.csv` — 83 839 B · 648 filas · ene 2023–dic 2025
- `conjunto_de_datos/bcmm_mensual_tr_cifra_2026.csv` — 18 131 B · 141 filas · ene–ago 2026; última fila `Cifras Oportunas`
- `catalogos/tc_periodo_mes.csv` — 170 B · 12 filas
- `diccionario_de_datos/diccionario_datos_bcmm_mensual_2012_2026.csv` — 1 898 B · 8 filas
- `metadatos/metadatos_bcmm_mensual_2012_2022.txt`, `…_2023_2025.txt`, `…_2026.txt`
- `modelo_entidad_relacion/modelo_er_bcmm_mensual_2012_2026.png`

ZIP hermano, no extraído aquí: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/bcmm_mensual_csv.zip — zip real, 66 482 B (3 oct 2026). Parte las tablas distinto (2012–2016 … 2025) y el diccionario llega a 2012–2025; no trae CSV de 2026. No es el mismo paquete.

## BCMM — mensual, modo de transporte (ZIP oficial)

- ZIP: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_mensual_mtra_csv.zip
- Sondeo 3 oct 2026: `application/x-zip-compressed` · 2 401 675 B · firma `PK`
- Programa: https://www.inegi.org.mx/programas/comext/
- Carpeta: `datos/mensual_mtra/`
- Forma: ZIP oficial
- Periodo en las tablas: enero 2012 a julio 2026
- Unidad (diccionario): `VAL_USD` en millones de dólares FOB
- Trae exportación e importación. Capítulo × medio de transporte y aduana × medio de transporte. No es país.

Archivos del ZIP (filas = datos, sin encabezado; tamaños releídos en el disco el 3 oct 2026):

- `conjunto_de_datos/bcmm_mtra_capitulo_mensual_tr_cifra_2012_2026.csv` — 26 752 913 B · 171 850 filas (85 925 exportación y 85 925 importación)
- `conjunto_de_datos/bcmm_mtra_aduana_mensual_tr_cifra_2012_2026.csv` — 1 842 836 B · 14 350 filas (7 175 por flujo)
- `catalogos/tc_mtra.csv` — 92 B · 5 filas
- `catalogos/tc_periodo_mes.csv` — 170 B · 12 filas
- `diccionario_de_datos/diccionario_datos_bcmm_mtra_mensual_2012_2026.csv` — 2 709 B · 10 filas
- `metadatos/metadatos_bcmm_mtra_mensual_2012_2026.txt`
- `modelo_entidad_relacion/modelo_er_bcmm_mtra_mensual_2012_2026.png`

## BCMM — mensual, país por tipo de bien (ZIP oficial)

- ZIP: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_mensual_paises_bien_csv.zip
- Sondeo 3 oct 2026: `application/x-zip-compressed` · 1 666 349 B · firma `PK`
- Programa: https://www.inegi.org.mx/programas/comext/
- Carpeta: `datos/mensual_paises_bien/`
- Forma: ZIP oficial
- Periodo: enero 2015 a julio 2026
- Unidad (diccionario): `VAL_USD` en miles de dólares FOB
- INEGI parte la tabla en tres CSV. Cada uno trae exportación e importación. País vacío = total de zona, no un país. No es capítulo.

Archivos del ZIP (filas = datos, sin encabezado; tamaños releídos en el disco el 3 oct 2026):

- `conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2015_2022.csv` — 27 268 595 B · 148 680 filas
- `conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2023_2025.csv` — 10 114 644 B · 55 728 filas
- `conjunto_de_datos/bcmm_paises_bien_mensual_tr_cifra_2026.csv` — 1 964 317 B · 10 836 filas
- `catalogos/tc_continente.csv` — 92 B · 5 filas
- `catalogos/tc_region.csv` — 375 B · 13 filas
- `catalogos/tc_pais.csv` — 4 645 B · 263 filas
- `catalogos/tc_periodo_mes.csv` — 170 B · 12 filas
- `diccionario_de_datos/diccionario_datos_paises_bien_mensual_2015_2026.csv` — 3 402 B · 12 filas
- `metadatos/metadatos_paises_bien_mensual_2015_2022.txt`, `…_2023_2025.txt`, `…_2026.txt`
- `modelo_entidad_relacion/modelo_er_paises_bien_mensual_2015_2026.png`

## BCMM — anual, tarifa × país (ZIP oficial)

- ZIP extraído en este repo: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_anual_csv.zip
- Sondeo 3 oct 2026: `application/x-zip-compressed` · 129 367 989 B · firma `PK`
- Programa: https://www.inegi.org.mx/programas/comext/
- Carpeta: `datos/anual/`
- Forma: ZIP oficial
- Periodo: 2003–2025, un CSV por año
- Unidad (diccionario): `VAL_USD` en dólares FOB (no millones ni miles). `VAL_MNX` en pesos. `CANTIDAD` según `UMED` de la TIGIE.
- Es tarifa (TIGIE) × país. No se junta con el mensual de capítulo, el mensual de país ni el mensual de agregados.

El `schema.org` de COMEXT nombra otro ZIP: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/bcmm_anual_csv.zip — zip real, 117 456 482 B (3 oct 2026). Ese paquete llega a 2023 (diccionario `…_2003_2023.csv`; no trae CSV 2024 ni 2025). No es el mismo paquete que el extraído aquí.

Tablas del ZIP `conjunto_de_datos_bcmm_anual_csv.zip` (`conjunto_de_datos/`):

| Archivo | Bytes | Filas | En git |
| --- | ---: | ---: | --- |
| `bcmm_anual_tr_cifra_2003.csv` | 77,615,671 | 477,762 | sí |
| `bcmm_anual_tr_cifra_2004.csv` | 80,306,977 | 494,178 | sí |
| `bcmm_anual_tr_cifra_2005.csv` | 78,683,405 | 499,691 | sí |
| `bcmm_anual_tr_cifra_2006.csv` | 80,132,385 | 508,488 | sí |
| `bcmm_anual_tr_cifra_2007.csv` | 134,471,337 | 850,431 | no (≥100 MB). Tabla anual completa: https://cubos-mx-datos.web.app/bcmm_anual_tr_cifra_2007.csv |
| `bcmm_anual_tr_cifra_2008.csv` | 83,818,325 | 531,719 | sí |
| `bcmm_anual_tr_cifra_2009.csv` | 83,074,751 | 527,411 | sí |
| `bcmm_anual_tr_cifra_2010.csv` | 86,067,766 | 546,193 | sí |
| `bcmm_anual_tr_cifra_2011.csv` | 87,270,477 | 553,553 | sí |
| `bcmm_anual_tr_cifra_2012.csv` | 148,298,369 | 937,415 | no (≥100 MB). Tabla anual completa: https://cubos-mx-datos.web.app/bcmm_anual_tr_cifra_2012.csv |
| `bcmm_anual_tr_cifra_2013.csv` | 90,978,590 | 576,870 | sí |
| `bcmm_anual_tr_cifra_2014.csv` | 91,819,364 | 582,172 | sí |
| `bcmm_anual_tr_cifra_2015.csv` | 82,592,591 | 586,316 | sí |
| `bcmm_anual_tr_cifra_2016.csv` | 83,968,027 | 595,817 | sí |
| `bcmm_anual_tr_cifra_2017.csv` | 84,573,569 | 600,079 | sí |
| `bcmm_anual_tr_cifra_2018.csv` | 86,476,361 | 613,814 | sí |
| `bcmm_anual_tr_cifra_2019.csv` | 86,449,821 | 613,400 | sí |
| `bcmm_anual_tr_cifra_2020.csv` | 82,921,215 | 588,647 | sí |
| `bcmm_anual_tr_cifra_2021.csv` | 91,097,469 | 632,907 | sí |
| `bcmm_anual_tr_cifra_2022.csv` | 122,775,704 | 850,011 | no (≥100 MB). Tabla anual completa: https://cubos-mx-datos.web.app/bcmm_anual_tr_cifra_2022.csv |
| `bcmm_anual_tr_cifra_2023.csv` | 121,778,100 | 842,912 | no (≥100 MB). Tabla anual completa: https://cubos-mx-datos.web.app/bcmm_anual_tr_cifra_2023.csv |
| `bcmm_anual_tr_cifra_2024.csv` | 120,315,175 | 832,608 | no (≥100 MB). Tabla anual completa: https://cubos-mx-datos.web.app/bcmm_anual_tr_cifra_2024.csv |
| `bcmm_anual_tr_cifra_2025.csv` | 120,346,046 | 832,768 | no (≥100 MB). Tabla anual completa: https://cubos-mx-datos.web.app/bcmm_anual_tr_cifra_2025.csv |

También en el ZIP: catálogos, diccionario, metadatos y modelo (detalle en [CATALOGOS.md](CATALOGOS.md)).

## ETEF — anual por entidad y subsector (ZIP oficial)

No es BCMM. No se dobla en los CSV de COMEXT.

- ZIP: https://www.inegi.org.mx/contenidos/programas/exporta_ef/datosabiertos/conjunto_de_datos_eef_csv.zip
- Sondeo 3 oct 2026: `application/x-zip-compressed` · 203 969 B · firma `PK`
- Programa vivo: https://www.inegi.org.mx/programas/exporta_ef/ (HTML 3 896 B; `schema.org` nombra este ZIP; `temporalCoverage` del JSON: 2023)
- Tema: https://www.inegi.org.mx/temas/exportacionesef/ (HTML 2 656 B). Aviso en la página: desde el 30 de septiembre de 2025 el desglose trimestral y anual por sector y subsector SCIAN «solo se encuentra disponible en los tabulados interactivos y Banco de Información Económica (BIE)». Aun así este ZIP de datos abiertos existe y se bajó.
- Programa muerto: https://www.inegi.org.mx/programas/exportacionesef/ — «Esta liga ya no existe»
- BIE: https://www.inegi.org.mx/sistemas/bie/ — HTTP 500 el 3 oct 2026
- Carpeta: `datos/etef_anual/`
- Forma: ZIP oficial
- Periodo (diccionario y primera/última fila): 2007–2025. Metadato: `temporal: 2007-01-01-2025-12-31`; `modified: 2026-03-31T06:00`
- Unidad (diccionario): `VAL_USD` en miles de dólares FOB
- SCIAN 2007, entidad (`CVE_ENT`). `CODIGO_SCIAN` 000 = subsectores no publicados por confidencialidad.

Archivos del ZIP (filas = datos, sin encabezado):

- `conjunto_de_datos/eef_estatal_anual_tr_cifra_2007_2025.csv` — 2 008 293 B · 16 416 filas
- `catalogos/tc_entidad.csv` — 543 B · 33 filas
- `catalogos/tc_scian.csv` — 1 526 B · 27 filas
- `diccionario_de_datos/diccionario_datos_eef_anual_2007_2025.csv` — 2 383 B · 8 filas
- `metadatos/metadatos_eef_anual_2007_2025.txt`
- `modelo_entidad_relacion/modelo_er_eef_anual_2007_2025.png`

## ETEF — trimestral por entidad y subsector (ZIP oficial)

- ZIP: https://www.inegi.org.mx/contenidos/programas/exporta_ef/datosabiertos/conjunto_de_datos_eef_trimestral_csv.zip
- Sondeo 3 oct 2026: `application/x-zip-compressed` · 406 425 B · firma `PK`
- Programa: https://www.inegi.org.mx/programas/exporta_ef/ (el `schema.org` de esa página no nombra este ZIP; el archivo es zip real)
- Carpeta: `datos/etef_trimestral/`
- Forma: ZIP oficial
- Periodo (primera/última fila y metadato): 2007-I a 2026-II (`temporal: 2007-01-01-2026-06-30`; `modified: 2026-09-30T06:00`)
- Unidad (diccionario de este paquete): `VAL_USD` en dólares FOB, no en miles. No se suma con el anual ETEF ni con la BCMM.
- SCIAN 2007. Trae `CVEGEO` y `CVE_ENT`.

Archivos del ZIP (filas = datos, sin encabezado):

- `conjunto_de_datos/eef_trimestral_tr_cifra_2007_2026.csv` — 9 371 975 B · 67 392 filas
- `catalogos/tc_entidad.csv` — 626 B · 32 filas
- `catalogos/tc_periodo_mes.csv` — 108 B · 4 filas
- `catalogos/tc_scian.csv` — 1 526 B · 27 filas
- `diccionario_de_datos/diccionario_datos_eef_trimestral_2007_2026.csv` — 2 604 B · 11 filas
- `metadatos/metadatos_eef_trimestral_2007_2026.txt`
- `modelo_entidad_relacion/modelo_er_eef_trimestral_2007_2026.png`

## ETEF — histórico 2007–2016 (ZIP oficial, paquete viejo)

- ZIP: https://www.inegi.org.mx/contenidos/programas/exporta_ef/datosabiertos/eef_csv.zip
- Sondeo 3 oct 2026: `application/x-zip-compressed` · 80 976 B · firma `PK`
- El metadato interno apunta a `http://www.inegi.org.mx/est/contenidos/proyectos/registros/economicas/exporta_ef/doc/eef_2007_2016.zip` y `Modified: 2017-10-30`
- URL inventada `…/conjunto_de_datos_eef_historico_csv.zip`: HTML 2 263 B, no zip
- Carpeta: `datos/etef_historico_2007_2016/`
- Forma: ZIP oficial
- Periodo: 2007–2016
- Unidad (diccionario): `VAL_USD` en miles de dólares FOB
- No sustituye al anual 2007–2025 ni al trimestral.

Archivos del ZIP (filas = datos, sin encabezado):

- `conjunto_de_datos/eef_tr_cifra.csv` — 1 282 706 B · 8 000 filas
- `catalogos/tc_entidad.csv` — 523 B · 32 filas
- `diccionario_de_datos/diccionario_de_datos_eef.csv` — 2 193 B · 11 filas
- `metadatos/metadatos_eef.txt`
- `modelo_entidad_relacion/modelo_er_eef.png`

## INEGI OLAP — tipo × país × fracción (extracto de cubo)

- Consulta: 3 oct 2026
- Página abierta: https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/comex/comex_bcmm_mensual2023.asp
- Cubo hermano abierto el mismo día, no extraído: https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/comex/comex_bcmm_mensual2021_2022.asp
- Forma: extracto de cubo (`MDXQueryDatos.asp` + `exporta.aspx` CSV). No es ZIP oficial.
- Carpeta: `datos/olap_bcmm_mensual2023/`
- Periodo extraído: enero 2023 – julio 2026 (43 meses). La página no nombra agosto 2026.
- Unidad: dólares FOB (el CSV oficial también trae cantidad)
- Cruce: importación o exportación × país × fracción de 8 dígitos. El capítulo es el prefijo de la fracción.
- Completitud: cada mes, filas de datos = `Cant_Fil` del visor. Suma: 4 540 560 filas. Índice: `datos/olap_bcmm_mensual2023/indice.json`.

No se junta con el mensual de capítulo (millones) ni con el de país (miles). Notas: `datos/extractos/OLAP_capitulo_pais_fraccion.md`.

## Banxico — Cubo de Comercio Exterior (sin archivo completo)

- Consultas: 3 oct 2026 y 4 oct 2026, 02:06 UTC
- Página abierta: https://www.banxico.org.mx/CuboComercioExterior/ (HTTP 200, `text/html;charset=UTF-8`, 118 910 B; 0 href `.csv`/`.zip`)
- SIDIE: https://www.banxico.org.mx/DataSetsWeb/dataset?ruta=Cubo&idioma=es — HTTP 200, 4 283 B, texto «Todavía no existe ningún registro.»
- Tablero: https://tablero.banxico.org.mx/ — HTTP 401, `text/html;charset=utf-8`, 2 968 B, etiqueta `YOU DON'T HAVE THE AUTHORIZATION`
- Rutas de dump (`/datos.csv`, `/cubo.zip`, `/ValorDolares/csv`, `/ValorDolares/export`): HTTP 404, 103 B, `The resource you are looking for has been removed, had its name changed, or is temporarily unavailable.`
- Forma: software de consulta (embebe `tablero.banxico.org.mx`, Pyramid). La ayuda solo ofrece copiar al portapapeles o Imprimir → Excel de la tabla consultada.
- Unidad que declara la bienvenida: valor en dólares (tratamiento estadístico). Volumen solo a nivel fracción, sin tratamiento estadístico.
- Periodo: el tutorial usa desde enero 1993; las páginas abiertas no publican la fecha final.

No se publica un Excel truncado. No se recorre el tablero capítulo por capítulo. Los ZIP de SIDIE MLL no son este cubo. Tabla HTTP: `datos/extractos/BANXICO_cubo.md`. Sondeo: `datos/banxico_cubo/probe.json`.

## Catálogos y diccionarios

Cada CSV de `catalogos/` y `diccionario_de_datos/` es pieza del ZIP oficial de su paquete, no un extracto de cubo. Lista con URL, fecha, unidad y periodo: [CATALOGOS.md](CATALOGOS.md). No se reescribieron esos CSV.
