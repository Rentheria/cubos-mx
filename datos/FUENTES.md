# Recortes publicados

Solo exportación. El Excel no se guarda. Los ZIP originales de INEGI traen también importación.

## Capítulo por medio de transporte

- Archivo: `exportaciones_capitulo_transporte_2012_2026.csv`
- Fuente: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_mensual_mtra_csv.zip
- Programa: https://www.inegi.org.mx/programas/comext/
- Periodo en el archivo: enero 2012 a julio 2026
- Qué es: capítulo arancelario (texto en `CONCEPTO`) por medio de transporte (`MTRA`), nacional, no por país
- `VAL_USD` está en millones de dólares, FOB
- Se quitó importación. Quedaron 85,925 filas

## País por tipo de bien

- Archivo: `exportaciones_pais_tipo_bien_2015_2026.csv`
- Fuente: https://www.inegi.org.mx/contenidos/programas/comext/datosabiertos/conjunto_de_datos_bcmm_mensual_paises_bien_csv.zip
- Periodo: enero 2015 a julio 2026
- Qué es: país o zona (`PAIS_O_D`) por tipo de bien (consumo, intermedio, capital). No es capítulo
- `VAL_USD` está en miles de dólares
- Una fila con país vacío es el total de esa zona, no un país
- Se quitó importación. Quedaron 107,622 filas

No existe un CSV público de capítulo por país. Ese cruce solo está en el cubo:
https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/comex/comex_bcmm_mensual2023.asp
