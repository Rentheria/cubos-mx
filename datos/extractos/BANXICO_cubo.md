# Banxico — Cubo de Comercio Exterior

No hay un archivo oficial completo (CSV, ZIP ni otro dump entero). Esta página no es un substituto de ese archivo: es el registro de lo que respondió cada URL el 4 de octubre de 2026, 02:06 UTC, desde esta VM. Sondeo: `datos/banxico_cubo/probe.json`.

- Página del cubo: https://www.banxico.org.mx/CuboComercioExterior/
- Catálogo SIDIE: https://www.banxico.org.mx/DataSetsWeb/?idioma=es
- Tablero embebido: https://tablero.banxico.org.mx/no-shell/embed.js
- Comunicado (31 mar 2022): https://www.banxico.org.mx/publicaciones-y-prensa/miscelaneos/%7B5139DD05-D18B-1122-6D17-45C0CB888598%7D.pdf (HTTP 200, `application/pdf`, 126 864 B; anuncia la herramienta, no un dump)
- Unidad que declara la bienvenida: valor en dólares (tratamiento estadístico). Volumen solo a nivel fracción, sin tratamiento estadístico.
- Periodo que nombra el tutorial: desde enero 1993. Las páginas abiertas no publican la fecha final.

No se publica un Excel cortado. No se recorre el tablero capítulo por capítulo. No se junta con los ZIP de INEGI. No se inventa un cruce capítulo × país a partir de otros cortes.

## Qué ofreció Banxico (texto de las páginas 200)

La ayuda del cubo (`#pills-exportar`) solo describe dos salidas de **la tabla consultada**:

1. Clic derecho → Copiar contenido → Copiar datos sin procesar (portapapeles).
2. Clic derecho → Imprimir → Presentación completa o Diapositiva actual → Excel.

La misma ayuda avisa: si se pega a Excel y la consulta pasa el máximo de filas de Microsoft Office, se trunca. La página no nombra ese máximo.

SIDIE lista «Cubo de Información de Comercio Exterior» con el botón «Ir al sitio», que apunta otra vez a `CuboComercioExterior/`. La ficha del cubo en SIDIE no tiene ZIP.

## SIDIE: el cubo no tiene registro de archivo

`https://www.banxico.org.mx/DataSetsWeb/dataset?ruta=Cubo&idioma=es` respondió **HTTP 200** `text/html;charset=UTF-8` **4 283 B**. El texto visible es:

> Todavía no existe ningún registro.

Eso es el catálogo de datasets de Banxico diciendo que no hay archivo registrado para el cubo. No es una opinión de este repo.

Los ZIP que SIDIE sí publica (`dataset-9.zip`, `dataset-10.zip`, `dataset-11.zip`) están en `dataset?ruta=MLL` (mercados de trabajo locales). No son el cubo. No se publican aquí como si lo fueran.

`dataset?ruta=Balanza` (HTTP 200, 6 559 B) solo enlaza PDFs de balanza de pagos / SIE. Tampoco es el cubo.

## Tabla HTTP (4 oct 2026, 02:06 UTC)

Cuerpo 404 (103 B, `text/html`): `The resource you are looking for has been removed, had its name changed, or is temporarily unavailable.`

Cuerpo 401 del tablero: HTML Pyramid, etiqueta visible `YOU DON'T HAVE THE AUTHORIZATION`.

| URL | HTTP | Content-Type | Bytes | Qué se vio |
| --- | ---: | --- | ---: | --- |
| https://www.banxico.org.mx/CuboComercioExterior/ | 200 | text/html;charset=UTF-8 | 118 910 | Shell del cubo. 0 href `.csv`/`.zip`. Solo `embed.js` del tablero. |
| …/ValorDolares/inicio | 200 | text/html;charset=UTF-8 | 118 995 | Igual: visor, sin dump. |
| …/ValorDolaresAnual/inicio | 200 | text/html;charset=UTF-8 | 119 341 | Igual. |
| …/ValorDolares/seriesproducto | 200 | text/html;charset=UTF-8 | 118 917 | Igual. |
| …/ValorDolares/matrizprodregion | 200 | text/html;charset=UTF-8 | 118 923 | Igual. |
| …/ValorDolares/participacion | 200 | text/html;charset=UTF-8 | 118 818 | Igual. |
| …/ValorDolares/mapa | 200 | text/html;charset=UTF-8 | 118 901 | Igual. |
| …/ValorDolares/seriesregion | 200 | text/html;charset=UTF-8 | 118 916 | Igual. |
| …/Volumen/seriesproducto | 200 | text/html;charset=UTF-8 | 117 364 | Igual. |
| …/Volumen/inicio | 404 | text/html | 103 | Cuerpo 404 citado arriba. |
| …/Volumen/seriesregion | 404 | text/html | 103 | Cuerpo 404. |
| …/ValorDolares/export | 404 | text/html | 103 | Cuerpo 404. |
| …/ValorDolares/csv | 404 | text/html | 103 | Cuerpo 404. |
| …/ValorDolares/download | 404 | text/html | 103 | Cuerpo 404. |
| …/datos.csv | 404 | text/html | 103 | Cuerpo 404. |
| …/datos.zip | 404 | text/html | 103 | Cuerpo 404. |
| …/cubo.csv | 404 | text/html | 103 | Cuerpo 404. |
| …/cubo.zip | 404 | text/html | 103 | Cuerpo 404. |
| …/export.csv | 404 | text/html | 103 | Cuerpo 404. |
| …/export.zip | 404 | text/html | 103 | Cuerpo 404. |
| …/download | 404 | text/html | 103 | Cuerpo 404. |
| https://www.banxico.org.mx/files/CuboComercioExterior.zip | 404 | text/html | 103 | Cuerpo 404. |
| https://www.banxico.org.mx/files/cubo-comercio-exterior.csv | 404 | text/html | 103 | Cuerpo 404. |
| https://www.banxico.org.mx/DataSetsWeb/?idioma=es | 200 | text/html;charset=UTF-8 | 6 314 | Tres tarjetas. Cubo → `CuboComercioExterior/`. MLL sí tiene ZIP (no es el cubo). |
| https://www.banxico.org.mx/DataSetsWeb/dataset?ruta=Cubo&idioma=es | 200 | text/html;charset=UTF-8 | 4 283 | «Todavía no existe ningún registro.» |
| https://www.banxico.org.mx/DataSetsWeb/dataset?ruta=Balanza&idioma=es | 200 | text/html;charset=UTF-8 | 6 559 | PDFs de balanza de pagos. Sin CSV/ZIP del cubo. |
| https://www.banxico.org.mx/DataSetsWeb/dataset?ruta=MLL&idioma=es | 200 | text/html;charset=UTF-8 | 12 846 | ZIP de mercados laborales locales. No es el cubo. |
| https://www.banxico.org.mx/DataSetsWeb/cubo | 0 | — | 0 | `RemoteDisconnected: Remote end closed connection without response` |
| https://www.banxico.org.mx/DataSetsWeb/comercio | 0 | — | 0 | `RemoteDisconnected: Remote end closed connection without response` |
| https://tablero.banxico.org.mx/ | 401 | text/html;charset=utf-8 | 2 968 | Pyramid: `YOU DON'T HAVE THE AUTHORIZATION` |
| https://tablero.banxico.org.mx/no-shell/ | 401 | text/html;charset=utf-8 | 2 968 | Igual. |
| https://tablero.banxico.org.mx/no-shell/embed.js | 200 | text/javascript | 1 722 | Loader (`2025.11.226`). Pide cookie `PyramidEmbeddedAuth`. |
| https://tablero.banxico.org.mx/API/auth/login | 500 | (vacío) | 0 | Cuerpo vacío. |
| https://tablero.banxico.org.mx/API3/authentication/authenticateUserEmbed | 401 | text/html;charset=utf-8 | 1 484 | Misma página 401. |
| https://tablero.banxico.org.mx/API/export | 401 | text/html;charset=utf-8 | 2 968 | Misma página 401. |
| https://tablero.banxico.org.mx/API/download | 401 | text/html;charset=utf-8 | 2 968 | Misma página 401. |
| https://tablero.banxico.org.mx/export | 401 | text/html;charset=utf-8 | 2 968 | Misma página 401. |
| https://tablero.banxico.org.mx/csv | 401 | text/html;charset=utf-8 | 2 968 | Misma página 401. |
| https://www.banxico.org.mx/SieAPIRest/service/v1/ | 200 | application/json;charset=UTF-8 | 2 | `{}`. Series de tiempo; no es el cubo. |
| https://www.banxico.org.mx/SieInternet/ | 200 | text/html;charset=ISO-8859-1 | 41 040 | SIE, no el cubo. |
| https://www.snice.gob.mx/cs/avi/snice/fuentesestadisticas.html | 200 | text/html; charset=UTF-8 | 30 936 | Remite a `CuboComercioExterior/`. Sin archivo. |
| https://datos.gob.mx/busca/dataset?q=banxico+comercio+exterior | 403 | text/html | 384 | Akamai: `Access Denied` / `You don't have permission to access …/busca/dataset?` |
| https://historico.datos.gob.mx/busca/dataset/estadistica-de-comercio-exterior-importaciones-y-exportaciones-de-mexico | 403 | text/html | 506 | `Access Denied` (ese dataset es SE 2016/2017, no el cubo). |

Reenvío de cookies `JSESSIONID` de `CuboComercioExterior/` hacia `tablero.banxico.org.mx/`, `/no-shell/` y `/API3/authentication/authenticateUserEmbed`: otra vez **401**, misma etiqueta. El HTML del cubo no trae UUID de storyboard ni `PyramidEmbeddedAuth`.

## Qué no se hizo

- No se publicó un Excel de una consulta (Banxico avisa que Excel trunca).
- No se recorrió el tablero capítulo por capítulo.
- No se mezcló con `datos/mensual/`, `datos/mensual_mtra/` ni `datos/mensual_paises_bien/`.
- No se subió nada a Firebase.
