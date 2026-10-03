# cubos-mx

Catálogo de cubos públicos de México y las tablas oficiales de la Balanza Comercial de Mercancías de INEGI que caben en este repositorio.

Hoy cubre afiliación del IMSS, la balanza comercial de mercancías de INEGI y el cubo de comercio exterior de Banxico. El detalle, con periodos y qué no se puede mezclar, está en [CATALOGO.md](CATALOGO.md).

Las tablas de INEGI se consultan y se descargan en [consulta.html](consulta.html). Capítulo y país no se juntan. Millones, miles y dólares no se suman.

## Qué es y qué no

Cada cubo se consulta en su visor. Empleo formal y fracciones de exportación no viven en la misma tabla: no comparten grano ni llave.

No es un data lake. No hay app todavía.

## Fuentes

- IMSS, cubos de información: https://www.imss.gob.mx/conoce-al-imss/cubos
- INEGI, balanza comercial de mercancías: https://www.inegi.org.mx/programas/comext/
- Banxico, cubo de comercio exterior: https://www.banxico.org.mx/CuboComercioExterior/

Los números son de esas instituciones. Los archivos en [datos/](datos/) salen de los ZIP de datos abiertos de INEGI; el inventario está en [datos/FUENTES.md](datos/FUENTES.md).
