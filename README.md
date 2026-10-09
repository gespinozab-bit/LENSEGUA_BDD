# Laboratorio BDD de LENSEGUA

## Objetivo

Automatizar con `pytest-bdd`, `pytest` y Selenium el flujo crítico de publicación controlada de material educativo. El piloto valida que un docente pueda guardar borradores, publicar únicamente recursos completos y revisados, y desactivar material para retirarlo del portal estudiantil.

Este flujo es distinto del inicio de sesión y está alineado con los módulos actuales de LENSEGUA: Vocales, Números, Abecedario y Colores.

## Taller de tres amigos

Los escenarios fueron definidos desde tres perspectivas:

- **Negocio:** el docente necesita que únicamente el material autorizado sea visible para los estudiantes.
- **Desarrollo:** el formulario debe controlar campos obligatorios, estados y actualización de la vista estudiantil.
- **QA:** cada regla debe tener un resultado observable y automatizable.

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

## Revisión después del sprint

La revisión propuesta debe confirmar:

- El docente entiende los escenarios sin leer el código.
- Los mensajes coinciden con las reglas del proceso.
- Los borradores y contenidos inactivos no aparecen en el portal estudiantil.
- Solo el material revisado puede publicarse.
- Los cambios solicitados por negocio se incorporan al archivo `.feature` antes del siguiente sprint.

## Evidencia pendiente en GitHub

Después de subir esta carpeta a un repositorio, ejecute el workflow **Pruebas BDD LENSEGUA** y agregue en `Evidencias/` una captura de la ejecución completada. Esa captura confirma la ejecución real en CI y no debe sustituirse por una imagen simulada.
