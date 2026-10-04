# Recortes para descarga filtrada

Consulta 4 oct 2026. La página (`consulta.html` → Recorte) baja solo el año y el corte elegidos. No abre los CSV anuales de 100 MB o más.

| Corte | Unidad | Origen | Carpeta |
| --- | --- | --- | --- |
| Capítulo | millones de dólares FOB | ZIP modo de transporte | `capitulo_millones/YYYY.csv` |
| País | miles de dólares FOB | ZIP país × tipo de bien | `pais_miles/YYYY.csv` |
| Cruce OLAP | dólares FOB | extracto del cubo `COMEX_BCMM_MENSUAL_2023` | `olap_dolares/YYYY.csv.gz` |

Capítulo y país no se juntan. No se inventa un cruce capítulo × país a partir de esos dos ZIP. El cruce real es el OLAP (tipo × país × fracción, ene 2023–jul 2026).
