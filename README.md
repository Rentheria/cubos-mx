# cubos-mx

Catálogo de cubos públicos de México y las tablas oficiales de INEGI que caben en este repositorio.

Hoy cubre afiliación del IMSS, la balanza comercial de mercancías de INEGI (BCMM), las exportaciones por entidad federativa (ETEF) y el cubo de comercio exterior de Banxico. El inventario de cubos, con periodos y qué no se puede mezclar, está en [CATALOGO.md](CATALOGO.md). Los ZIP, catálogos y diccionarios, con URL, fecha de consulta, unidad y si son ZIP oficial o extracto de cubo, están en [datos/FUENTES.md](datos/FUENTES.md) y [datos/CATALOGOS.md](datos/CATALOGOS.md).

Las tablas se consultan y se descargan en [consulta.html](consulta.html) y en la copia publicada [https://rentheria.github.io/cubos-mx/consulta.html](https://rentheria.github.io/cubos-mx/consulta.html). Capítulo y país no se juntan. Millones, miles y dólares no se suman. ETEF no se dobla en la BCMM.

Consulta de las páginas y de los ZIP: 3 de octubre de 2026. Lo que el HTML de INEGI no lista se comprobó por `Content-Type` del archivo.

## Qué es y qué no

Cada cubo se consulta en su visor. Empleo formal, fracciones de la BCMM y exportaciones por entidad no viven en la misma tabla: no comparten grano ni llave.

No es un data lake. No hay app todavía.

El mensual de agregados BCMM (ZIP `conjunto_de_datos_bcmm_mensual_csv.zip`) trae agosto 2026 como cifra oportuna. El mensual de modo de transporte, el de país y el cubo OLAP 2023 siguen en julio 2026. No hay ZIP de entidad ni municipio en COMEXT: esas URLs inventadas son HTML.

El cubo OLAP 2023 (tipo × país × fracción, dólares FOB) sí se bajó por mes el 3 oct 2026: 43 CSV en `datos/olap_bcmm_mensual2023/`, enero 2023 a julio 2026. Banxico no publicó un CSV; `tablero.banxico.org.mx` respondió 401. Un Excel truncado no es el cubo.

## Fuentes

- IMSS, cubos de información: https://www.imss.gob.mx/conoce-al-imss/cubos
- INEGI, balanza comercial de mercancías: https://www.inegi.org.mx/programas/comext/
- INEGI, exportaciones por entidad federativa: https://www.inegi.org.mx/programas/exporta_ef/ (https://www.inegi.org.mx/programas/exportacionesef/ ya no existe)
- Banxico, cubo de comercio exterior: https://www.banxico.org.mx/CuboComercioExterior/

Los números son de esas instituciones. Los archivos en [datos/](datos/) salen de ZIP de datos abiertos, salvo `datos/olap_bcmm_mensual2023/` (extracto de cubo OLAP) y `datos/extractos/` (notas).
