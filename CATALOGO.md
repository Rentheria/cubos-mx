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

## INEGI, ENOE (tabulados interactivos)

INEGI los llama cubos. Notas (26 ago 2025): https://www.inegi.org.mx/sistemas/olap/proyectos/bd/encuestas/hogares/enoe/2010_pe_ed15/metadatos/enoe_notas_cubos.pdf
Cobertura que declara cada página: I 2005–I 2020 y desde I 2023 (ENOE); III 2020–IV 2022 (ENOE N). No son la balanza.

1. Población ocupada, 15 años y más. https://www.inegi.org.mx/sistemas/olap/proyectos/bd/encuestas/hogares/enoe/2010_pe_ed15/po.asp?p=enoe_pe_ed15&proy=enoe_pe_ed15_po&s=est
2. Población desocupada. https://www.inegi.org.mx/sistemas/olap/proyectos/bd/encuestas/hogares/enoe/2010_pe_ed15/pda.asp?p=enoe_pe_ed15&proy=enoe_pe_ed15_pda&s=est
3. Población no económicamente activa. https://www.inegi.org.mx/sistemas/olap/proyectos/bd/encuestas/hogares/enoe/2010_pe_ed15/pnea.asp?p=enoe_pe_ed15&proy=enoe_pe_ed15_pnea&s=est
4. Población total. https://www.inegi.org.mx/sistemas/olap/proyectos/bd/encuestas/hogares/enoe/2010_pe_ed15/pt.asp?p=enoe_pe_ed15&proy=enoe_pe_ed15_pt&s=est
5. Trabajador subordinado y remunerado. https://www.inegi.org.mx/sistemas/olap/proyectos/bd/encuestas/hogares/enoe/2010_pe_ed15/tsr.asp?p=enoe_pe_ed15&proy=enoe_pe_ed15_tsr&s=est

Las notas también nombran Población subocupada y Trabajador independiente. No apareció una URL que abriera.

## Secretaría de Salud, SINBA

Una página: https://sinba.salud.gob.mx/CubosDinamicos
No es IMSS ni el OLAP de INEGI. Cada bloque es un cubo; cada año es un archivo del mismo cubo.

- Egresos hospitalarios (SAEH): SSA 2000–2026 (2026 preliminar; desde 2024 incluye IMSS-Bienestar); sector salud 2004–2024.
- Defunciones INEGI/SS 1998–2024; muertes maternas 2002–2024; muertes fetales 1985–2024.
- Lesiones y violencia, SSA/IMSS-Bienestar, 2010–2026 (2026 preliminar).
- Nacidos vivos registrados, INEGI, 1990–2013. Nacimientos ocurridos, SINAC, 2008–agosto 2026.
- Recursos humanos, físicos y financieros, servicios otorgados (SIS), urgencias 2007–2026, establecimientos 2012–2019, proyecciones CONAPO.

## Buscado y no es otro cubo

- COMEX: el PDF de consulta interactiva lista solo los 9 ya catalogados. No hay cubo aparte de aduana, modo de transporte ni entidad. https://www.inegi.org.mx/contenidos/programas/comext/doc/descripcion.pdf
- IMSS: no hay un segundo visor. Cognos no abrió.
- Banxico: valor y volumen son secciones del mismo cubo.
- SAT/SNICE remite a Banxico e INEGI. CONEVAL son Excel, no OLAP.
- DataMéxico (api.datamexico.org/ui) devolvió 500. Sin lista verificada.
