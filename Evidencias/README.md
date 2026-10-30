# Evidencias del laboratorio BDD

| Requisito | Evidencia | Estado |
| --- | --- | --- |
| Piloto | Publicación controlada de material educativo; objetivo en el README principal | Documentado |
| Taller de tres amigos y 5 a 10 escenarios | Siete escenarios y [análisis de los tres roles](taller-tres-amigos.md) | Documentado como ejercicio académico |
| Automatización | `tests/test_publicacion_contenido.py`, con pytest-bdd, pytest y Selenium | Implementada; siete pruebas aprobadas en la validación local |
| CI con resultados visibles | Workflow Pruebas BDD LENSEGUA y captura real en GitHub | Completado |
| Revisión tras un sprint | [Revisión académica del piloto](revision-sprint.md) | Guía aplicada a los escenarios y resultados |

## Ejecución real de GitHub Actions

- [Ejecución #2 aprobada, correspondiente a la captura](https://github.com/gespinozab-bit/LENSEGUA_BDD/actions/runs/41082429592).
- [Captura real subida al repositorio](https://github.com/gespinozab-bit/LENSEGUA_BDD/blob/main/Evidencias/Captura%20de%20pantalla%202026-10-30%20093906.png).
- [Ejecución posterior a la subida de la evidencia, también aprobada](https://github.com/gespinozab-bit/LENSEGUA_BDD/actions/runs/41082920074).

La captura se llama `Captura de pantalla 2026-10-30 093906.png`. No es necesario
renombrarla. La primera ejecución fallida se conserva en el historial, pero las
ejecuciones aprobadas enlazadas arriba acreditan el cumplimiento.

Los reportes locales no sustituyen la captura real de GitHub Actions.
El workflow local está configurado para publicar reportes HTML y JUnit como
artefacto `resultados-bdd-lensegua`; comprobar su disponibilidad en cada ejecución.

## Alcance académico

Según la aclaración del estudiante, el taller y la revisión son referencias de
la guía para analizar el flujo elegido dentro del sistema. Los documentos
desarrollan las perspectivas de negocio, desarrollo y QA y la revisión de las
reglas del piloto. No se requieren actas de reuniones para este alcance ni se
atribuyen aprobaciones a personas externas.
