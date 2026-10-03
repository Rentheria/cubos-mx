# Catálogo de cubos (3 oct 2026)

Inventario, no datos. Una fila es un cubo o una consulta nombrada. Cognos del IMSS no abrió (timeout).

## IMSS

Un solo visor: https://www.imss.gob.mx/conoce-al-imss/cubos
Cognos (no verificado): http://cognos.imss.gob.mx/cubo_cp.asp
Guía: https://www.imss.gob.mx/sites/all/statics/pdf/informes/GuiaCubo.pdf
Calendario (11 dic 2025): https://www.imss.gob.mx/sites/all/statics/pdf/informes/Calendario_difusion.pdf

El portal no nombra consultas. El calendario nombra tres, todas en Medidas de Incorporación y Recaudación. Exportar el recorte: Archivo → PDF, CSV o XLS (según la guía, no visto dentro de Cognos). Grano: una cifra × mes × delegación (o nacional). No es balanza ni TIGIE.

1. Puestos de trabajo y asegurados sin un empleo asociado. Mensual desde julio 1997. Difusión antes del día 9. Sexo, edad, modalidad, tipo de puesto, régimen, actividad, tamaño patronal. Es stock de puestos, no personas únicas.
2. Dinámica laboral y patrones. Mensual desde agosto 1997. Altas, bajas, reingresos, contratación y separación, salario base. Rango en veces UMA solo desde enero 2017 (antes era salario mínimo). No mezclar con el stock de la fila 1.
3. Población derechohabiente adscrita y población potencial. PDA desde enero 2004; potencial desde julio 1997. Difusión antes del día 23. La PDA anterior a junio 2011 cambió de fuente y de método.

No hay fila médica: el glosario define términos (egresos, partos, quejas) pero no los presenta como carpetas.

Datos abiertos, aparte, no son el cubo: http://datos.imss.gob.mx/

## INEGI, balanza comercial de mercancías (BCMM)

Programa: https://www.inegi.org.mx/programas/comext/
Cada cubo corta en un cambio de tarifa. Celda: valor FOB o cantidad, de un flujo (importación o exportación) × país × código, en un año o un mes. "C" = uno o dos informantes, no es cero. La cantidad no se suma entre unidades distintas. Ninguna página nombró el botón; el catálogo solo dice "diversos formatos".

No hay cubo mensual anterior a enero 2021.

1. Comercio Exterior 1998 – ene a mar 2002. Anual, 2002 incompleto. Códigos a 8. Dólares o pesos, y cantidad. TIGE/TIGI 1 jul 1988, SA 1996. Definitivas. Sin NICO.
   https://www.inegi.org.mx/sistemas/olap/proyectos/bd/continuas/comex/comex1998_2002.asp?c=11004&proy=comex_98-02&s=est
2. abr 2002 – jun 2007. 2002 y 2007 incompletos. TIGIE 1 abr 2002, SA 2002. Definitivas.
   https://www.inegi.org.mx/sistemas/olap/proyectos/bd/continuas/comex/comex2002_2007.asp?c=11005&proy=comex_02-07&s=est
3. jul a dic 2007. Medio año. TIGIE 1 jul 2007, SA 2007. Definitivas.
   https://www.inegi.org.mx/sistemas/olap/proyectos/bd/continuas/comex/comex2007.asp?c=14293&proy=comex_07&s=est
4. 2008 – jun 2012. 2012 incompleto. Misma TIGIE 1 jul 2007, SA 2007. Definitivas.
   https://www.inegi.org.mx/sistemas/olap/proyectos/bd/continuas/comex/comex2008.asp?c=23720&proy=comex_08-09&s=est
5. jul 2012 – 2020. 2012 incompleto. TIGIE 1 jul 2012, SA 2012. Definitivas. Petróleo por continente, fuente PMI.
   https://www.inegi.org.mx/sistemas/olap/proyectos/bd/continuas/comex/comex2012.asp
6. Anual 2021–2022. TIGIE 28 dic 2020, SA 2017. Definitivas. NICO (10) entra; la fracción de 8 solo está en 2022.
   https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/comex/comex_bcmm.asp
7. Anual 2023–2025. TIGIE 12 dic 2022, SA 2022. La página dice definitivas. Choca con el mensual, que marca 2025 como revisada.
   https://www.inegi.org.mx/sistemas/olap/proyectos/bd/continuas/comex/comex_bcmm_2023.asp
8. Mensual ene 2021 – dic 2022. Solo dólares (no menciona pesos) y cantidad. TIGIE 28 dic 2020, SA 2017. Definitivas. Fracción de 8 solo en 2022.
   https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/comex/comex_bcmm_mensual2021_2022.asp
9. Mensual ene 2023 – jul 2026. Solo dólares FOB y cantidad. TIGIE 12 dic 2022, SA 2022. Definitivas 2023 y 2024; desde 2025, revisadas.
   https://www.inegi.org.mx/sistemas/Olap/Proyectos/bd/continuas/comex/comex_bcmm_mensual2023.asp

No son comparables de punta a punta. Un código de 6 dígitos puede cambiar de significado entre cubos.

Aparte, no es este cubo: exportaciones por entidad federativa (SCIAN, tabulados y BIE, no OLAP). https://inegi.org.mx/temas/exportacionesef/

## Banxico

Cubo de Comercio Exterior. https://www.banxico.org.mx/CuboComercioExterior/
El tutorial usa desde enero 1993. No publica la fecha final. Valor en dólares (tratamiento estadístico) por flujo, periodo, región o país, y producto. Volumen solo a nivel fracción. Exportar el recorte: clic derecho, copiar datos, o Imprimir → Excel. Excel trunca si la consulta es muy grande. Preliminar; puede no coincidir con la BCMM.

## No son cubos

BIE (INEGI) y SIE (Banxico): series agregadas de la balanza, no cubos.

## Falta confirmar dentro del visor

- Cognos: si hay carpetas médicas además de Incorporación y Recaudación.
- OLAP INEGI: el botón real de exportación y qué se puede arrastrar.
- Banxico: último periodo cargado, y si el valor anual se corta a fracción.
- 2025: el anual dice definitivas y el mensual dice revisadas.
