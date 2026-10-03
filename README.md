# cubos-mx

Catálogo de cubos públicos de México para sacar solo el recorte que hace falta, no el archivo entero.

Hoy cubre afiliación del IMSS, la balanza comercial de mercancías de INEGI y el cubo de comercio exterior de Banxico. El detalle, con periodos y qué no se puede mezclar, está en [CATALOGO.md](CATALOGO.md).

Los recortes CSV ya publicados de la balanza se consultan y se descargan en [consulta.html](consulta.html). Capítulo y país no se juntan. Millones y miles no se suman.

## Qué es y qué no

Cada cubo se consulta y se exporta el pedazo que pide el análisis. Empleo formal y fracciones de exportación no viven en la misma tabla: no comparten grano ni llave.

No es un data lake. No hay app todavía. El siguiente paso, cuando haya un recorte, es guardarlo en DuckDB y Parquet. Una interfaz en Next viene después, solo para leer esa tabla.

## Fuentes

- IMSS, cubos de información: https://www.imss.gob.mx/conoce-al-imss/cubos
- INEGI, balanza comercial de mercancías: https://www.inegi.org.mx/programas/comext/
- Banxico, cubo de comercio exterior: https://www.banxico.org.mx/CuboComercioExterior/

Los números son de esas instituciones. Los CSV en [datos/](datos/) son recortes de INEGI; el detalle está en [datos/FUENTES.md](datos/FUENTES.md).
