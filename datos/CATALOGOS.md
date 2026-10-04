# Catálogos y diccionarios (consulta 3 oct 2026)

Cada archivo de esta lista salió de un ZIP oficial de INEGI. Ninguno es extracto de cubo. No se reescribieron los CSV oficiales. Filas = datos, sin encabezado, contadas en el archivo extraído.

Unidad: los catálogos son claves (sin `VAL_USD`). El diccionario de cada paquete declara la unidad de `VAL_USD` de las tablas de hechos.

## BCMM mensual, agregados

ZIP: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_mensual_csv.zip  
Programa: https://www.inegi.org.mx/programas/comext/  
Consulta: 3 oct 2026 · forma: ZIP oficial · periodo del paquete: 2012–2026 (agosto 2026 oportunas) · unidad de las tablas: millones de dólares FOB

| Archivo | Bytes | Filas | Qué es |
| --- | ---: | ---: | --- |
| `datos/mensual/catalogos/tc_periodo_mes.csv` | 170 | 12 | Meses 01–12 |
| `datos/mensual/diccionario_de_datos/diccionario_datos_bcmm_mensual_2012_2026.csv` | 1 898 | 8 | Columnas; `VAL_USD` en millones de dólares FOB |

## BCMM mensual, modo de transporte

ZIP: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_mensual_mtra_csv.zip  
Programa: https://www.inegi.org.mx/programas/comext/  
Consulta: 3 oct 2026 · forma: ZIP oficial · periodo: ene 2012–jul 2026 · unidad de las tablas: millones de dólares FOB

| Archivo | Bytes | Filas | Qué es |
| --- | ---: | ---: | --- |
| `datos/mensual_mtra/catalogos/tc_mtra.csv` | 92 | 5 | Modos: Marítimo, Aéreo, Ferroviario, Carretero, Otros modos |
| `datos/mensual_mtra/catalogos/tc_periodo_mes.csv` | 170 | 12 | Meses 01–12 |
| `datos/mensual_mtra/diccionario_de_datos/diccionario_datos_bcmm_mtra_mensual_2012_2026.csv` | 2 709 | 10 | Columnas; `VAL_USD` en millones de dólares FOB |

## BCMM mensual, país por tipo de bien

ZIP: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_mensual_paises_bien_csv.zip  
Programa: https://www.inegi.org.mx/programas/comext/  
Consulta: 3 oct 2026 · forma: ZIP oficial · periodo: ene 2015–jul 2026 · unidad de las tablas: miles de dólares FOB

| Archivo | Bytes | Filas | Qué es |
| --- | ---: | ---: | --- |
| `datos/mensual_paises_bien/catalogos/tc_continente.csv` | 92 | 5 | Continentes |
| `datos/mensual_paises_bien/catalogos/tc_region.csv` | 375 | 13 | Zonas |
| `datos/mensual_paises_bien/catalogos/tc_pais.csv` | 4 645 | 263 | Países (`PAIS_O_D`) |
| `datos/mensual_paises_bien/catalogos/tc_periodo_mes.csv` | 170 | 12 | Meses 01–12 |
| `datos/mensual_paises_bien/diccionario_de_datos/diccionario_datos_paises_bien_mensual_2015_2026.csv` | 3 402 | 12 | Columnas; `VAL_USD` en miles de dólares FOB |

## BCMM anual, tarifa × país

ZIP extraído: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_anual_csv.zip  
Programa: https://www.inegi.org.mx/programas/comext/  
Consulta: 3 oct 2026 · forma: ZIP oficial · periodo: 2003–2025 · unidad de las tablas: dólares FOB y pesos (`VAL_MNX`)

El `schema.org` de COMEXT nombra `bcmm_anual_csv.zip` (117 456 482 B, llega a 2023). Ese no es este paquete.

| Archivo | Bytes | Filas | Qué es |
| --- | ---: | ---: | --- |
| `datos/anual/catalogos/tc_codigo_pais.csv` | 4 639 | 263 | Países |
| `datos/anual/catalogos/tc_periodo_mes.csv` | 131 | 14 | Periodos de mes del paquete anual |
| `datos/anual/catalogos/tc_tigie.csv` | 60 660 819 | 699 136 | Tarifa TIGIE |
| `datos/anual/catalogos/tc_unidad_medida.csv` | 226 | 15 | Unidades de medida |
| `datos/anual/diccionario_de_datos/diccionario_datos_bcmm_anual_2003_2025.csv` | 3 806 | 13 | Columnas; `VAL_USD` en dólares FOB |

`tc_tigie.csv`: 699 137 líneas en el archivo; 699 136 filas de datos si la primera es encabezado.

## ETEF anual

ZIP: https://www.inegi.org.mx/contenidos/programas/exporta_ef/datosabiertos/conjunto_de_datos_eef_csv.zip  
Programa: https://www.inegi.org.mx/programas/exporta_ef/  
Consulta: 3 oct 2026 · forma: ZIP oficial · periodo: 2007–2025 · unidad de las tablas: miles de dólares FOB

| Archivo | Bytes | Filas | Qué es |
| --- | ---: | ---: | --- |
| `datos/etef_anual/catalogos/tc_entidad.csv` | 543 | 33 | Entidades (`CVE_ENT`) |
| `datos/etef_anual/catalogos/tc_scian.csv` | 1 526 | 27 | Subsectores SCIAN 2007 |
| `datos/etef_anual/diccionario_de_datos/diccionario_datos_eef_anual_2007_2025.csv` | 2 383 | 8 | Columnas; `VAL_USD` en miles de dólares FOB |

## ETEF trimestral

ZIP: https://www.inegi.org.mx/contenidos/programas/exporta_ef/datosabiertos/conjunto_de_datos_eef_trimestral_csv.zip  
Programa: https://www.inegi.org.mx/programas/exporta_ef/  
Consulta: 3 oct 2026 · forma: ZIP oficial · periodo: 2007-I–2026-II · unidad de las tablas: dólares FOB (no miles)

| Archivo | Bytes | Filas | Qué es |
| --- | ---: | ---: | --- |
| `datos/etef_trimestral/catalogos/tc_entidad.csv` | 626 | 32 | `CVEGEO`, `CVE_ENT`, nombre |
| `datos/etef_trimestral/catalogos/tc_periodo_mes.csv` | 108 | 4 | Trimestres 01-03 … 10-12 |
| `datos/etef_trimestral/catalogos/tc_scian.csv` | 1 526 | 27 | Subsectores SCIAN 2007 |
| `datos/etef_trimestral/diccionario_de_datos/diccionario_datos_eef_trimestral_2007_2026.csv` | 2 604 | 11 | Columnas; `VAL_USD` en dólares FOB |

## ETEF histórico 2007–2016

ZIP: https://www.inegi.org.mx/contenidos/programas/exporta_ef/datosabiertos/eef_csv.zip  
Consulta: 3 oct 2026 · forma: ZIP oficial · periodo: 2007–2016 · unidad de las tablas: miles de dólares FOB

| Archivo | Bytes | Filas | Qué es |
| --- | ---: | ---: | --- |
| `datos/etef_historico_2007_2016/catalogos/tc_entidad.csv` | 523 | 32 | Entidades |
| `datos/etef_historico_2007_2016/diccionario_de_datos/diccionario_de_datos_eef.csv` | 2 193 | 11 | Columnas; `VAL_USD` en miles de dólares FOB |

## Cubos

OLAP INEGI: el extracto en `datos/olap_bcmm_mensual2023/` es el CSV del visor (tipo × país × fracción), no un catálogo aparte. Banxico no publicó catálogo ni CSV el 3 oct 2026. Notas: `datos/extractos/`.
