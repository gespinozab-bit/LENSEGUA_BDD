# Laboratorio BDD de LENSEGUA

## Objetivo

Automatizar con `pytest-bdd`, `pytest` y Selenium el flujo crítico de publicación controlada de material educativo. El piloto valida que un docente pueda guardar borradores, publicar únicamente recursos completos y revisados, y desactivar material para retirarlo del portal estudiantil.

Este flujo es distinto del inicio de sesión y está alineado con los módulos actuales de LENSEGUA: Vocales, Números, Abecedario y Colores.

## Taller de tres amigos

Los escenarios fueron definidos desde tres perspectivas:

- **Negocio:** el docente necesita que únicamente el material autorizado sea visible para los estudiantes.
- **Desarrollo:** el formulario debe controlar campos obligatorios, estados y actualización de la vista estudiantil.
- **QA:** cada regla debe tener un resultado observable y automatizable.

En este laboratorio, los tres amigos son una guía académica para analizar el
flujo elegido desde negocio, desarrollo y QA. El análisis aplicado está en
[Taller de tres amigos](Evidencias/taller-tres-amigos.md).

## Escenarios automatizados

El archivo `features/publicacion_contenido.feature` contiene siete escenarios:

1. Guardar un contenido como borrador.
2. Publicar un contenido completo y revisado.
3. Impedir la publicación sin módulo.
4. Impedir la publicación sin título.
5. Impedir la publicación sin recurso multimedia.
6. Impedir la publicación de material no revisado.
7. Desactivar un contenido publicado.

## Estructura

```text
LENSEGUA_BDD/
├── .github/workflows/tests.yml
├── app/
│   ├── contenidos.html
│   ├── contenidos.js
│   └── styles.css
├── features/publicacion_contenido.feature
├── tests/test_publicacion_contenido.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Ejecución local

1. Crear y activar un entorno virtual.
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Tener Google Chrome instalado.
4. Ejecutar:

```bash
pytest
```

Resultado esperado: `7 passed`.

Para generar los mismos reportes configurados en CI:

```bash
pytest --html=reportes/reporte-bdd.html --self-contained-html --junitxml=reportes/resultados.xml
```

## Integración continua

El workflow `.github/workflows/tests.yml` ejecuta los escenarios en cada `push`, `pull_request` o inicio manual. Configura Python 3.12, Chrome y ChromeDriver, instala las dependencias, ejecuta las pruebas y publica el reporte HTML y el resultado JUnit como artefactos descargables.

En CI, Selenium recibe las rutas de Chrome y ChromeDriver mediante
`CHROME_BIN` y `CHROMEDRIVER_PATH` desde el paso de instalación. En local,
si no se definen estas variables, Selenium detecta el navegador automáticamente.

## Revisión después del sprint

La [revisión académica del piloto](Evidencias/revision-sprint.md) aplica las
preguntas de la guía a los siete escenarios y sus resultados observables.

Los criterios de revisión son:

- El docente entiende los escenarios sin leer el código.
- Los mensajes coinciden con las reglas del proceso.
- Los borradores y contenidos inactivos no aparecen en el portal estudiantil.
- Solo el material revisado puede publicarse.
- Los cambios solicitados por negocio se incorporan al archivo `.feature` antes del siguiente sprint.

## Evidencia de GitHub Actions

Estado: **completado para el requisito de ejecución y captura en CI**.

El workflow **Pruebas BDD LENSEGUA** terminó correctamente en la
[ejecución #2](https://github.com/gespinozab-bit/LENSEGUA_BDD/actions/runs/41082429592).
La [captura real](https://github.com/gespinozab-bit/LENSEGUA_BDD/blob/main/Evidencias/Captura%20de%20pantalla%202026-10-30%20093906.png)
está en `Evidencias/` del repositorio. La ejecución posterior a su subida también
terminó correctamente.

Repositorio: https://github.com/gespinozab-bit/LENSEGUA_BDD.
Consulte [Evidencias/README.md](Evidencias/README.md) para la correspondencia
entre los cinco puntos de la guía y los entregables del laboratorio.
