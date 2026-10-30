# Revisión académica del piloto

Aplicación del punto «revisar tras un sprint» de la guía al flujo de publicación
de contenidos de LENSEGUA. El análisis se basa en los escenarios implementados y
su validación técnica; no atribuye una lectura o aprobación a un cliente externo.

## Alcance de la revisión

| Aspecto | Referencia |
| --- | --- |
| Piloto | Publicación controlada de material educativo |
| Alcance | Guardar borradores, publicar con validaciones y desactivar contenidos |
| Reglas revisadas | Siete escenarios en `features/publicacion_contenido.feature` |
| Verificación | Pruebas automatizadas y ejecución correcta en GitHub Actions |

## Material disponible

- [Siete escenarios de negocio](../features/publicacion_contenido.feature).
- [Pasos automatizados](../tests/test_publicacion_contenido.py).
- [Ejecución correcta en CI](https://github.com/gespinozab-bit/LENSEGUA_BDD/actions/runs/41082429592).
- [Captura real](https://github.com/gespinozab-bit/LENSEGUA_BDD/blob/main/Evidencias/Captura%20de%20pantalla%202026-10-30%20093906.png).

## Revisión desde la perspectiva de negocio

Para el ejercicio se comprueba que cada escenario describe una regla del flujo
e incluye un resultado que el docente o el estudiante puede observar.

| Escenario | Regla revisada | Resultado descrito y comprobado |
| --- | --- | --- |
| Guardar borrador | Preparar contenido sin publicarlo | Guardado, estado Borrador y ausencia en el portal |
| Publicar contenido completo y revisado | Exigir módulo, título, recurso y revisión | Estado Publicado y título visible para estudiantes |
| Publicación sin módulo | No publicar contenido sin clasificación | Mensaje de módulo obligatorio y portal sin contenido |
| Publicación sin título | No publicar contenido sin identificación | Mensaje de título obligatorio y portal sin contenido |
| Publicación sin recurso | No publicar contenido sin multimedia | Mensaje de recurso obligatorio y portal sin contenido |
| Publicación sin revisión | No publicar material sin confirmar revisión | Mensaje de revisión obligatoria y portal sin contenido |
| Desactivar contenido | Retirar material de la vista estudiantil | Estado Inactivo y ausencia en el portal |

## Correcciones y validación

Los siete escenarios actuales describen las reglas del piloto y sus resultados
observables. Esta revisión documental no introduce cambios en las reglas ni en
las pruebas. Se mantiene el alcance implementado y validado en CI.

Para una siguiente iteración, cualquier cambio en las reglas se refleja primero
en el `.feature`, luego en los pasos o la aplicación y se verifica nuevamente en
GitHub Actions. Por ejemplo, si se decidiera exigir un dato adicional al publicar,
habría que agregar o corregir el escenario correspondiente antes de implementarlo.

## Respuesta a la guía

La pregunta «¿negocio leyó y corrigió los escenarios?» se aplica aquí como una
comprobación académica de que los ejemplos expresan el comportamiento esperado
del sistema en términos del docente y del estudiante. La tabla anterior realiza
ese análisis y explica qué mantener y cómo incorporar futuras correcciones.
