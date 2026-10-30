# Taller de tres amigos

Aplicación académica de la guía de tres amigos al escenario elegido dentro de
LENSEGUA. Se analizan tres perspectivas complementarias sobre el mismo flujo.

## Piloto y perspectivas

Publicación controlada de material educativo de LENSEGUA. El docente guarda
borradores, publica recursos completos y revisados y desactiva material. Es
crítico porque determina qué contenido pueden consultar los estudiantes.

| Perspectiva | Aporte al piloto |
| --- | --- |
| Negocio | El docente prepara material y controla que solo los contenidos completos, revisados y publicados lleguen al estudiante. |
| Desarrollo | El formulario valida módulo, título, recurso y revisión; actualiza estados y visibilidad del portal. |
| QA | Convierte las reglas en siete ejemplos Given/When/Then y verifica mensajes, estados y presencia o ausencia en el portal. |

## Cobertura de los siete escenarios

Fuente: [publicacion_contenido.feature](../features/publicacion_contenido.feature).
La tabla conecta cada regla de negocio con su resultado observable.

| Escenario | Regla de negocio | Resultado observable para desarrollo y QA |
| --- | --- | --- |
| Guardar borrador | Preparar material sin publicarlo | Mensaje de guardado, estado Borrador y ausencia en el portal |
| Publicar contenido completo y revisado | Publicar material autorizado | Mensaje de publicación, estado Publicado y título visible en el portal |
| Impedir publicación sin módulo | Clasificar antes de publicar | Mensaje de módulo obligatorio y ausencia en el portal |
| Impedir publicación sin título | Identificar antes de publicar | Mensaje de título obligatorio y ausencia en el portal |
| Impedir publicación sin recurso | Exigir recurso multimedia | Mensaje de recurso obligatorio y ausencia en el portal |
| Impedir publicación sin revisión | Exigir revisión del material | Mensaje de revisión obligatoria y ausencia en el portal |
| Desactivar contenido publicado | Retirar material de la vista estudiantil | Mensaje de desactivación, estado Inactivo y ausencia en el portal |

## Resultado del análisis

| Pregunta de la guía | Aplicación al sistema |
| --- | --- |
| ¿El piloto representa un flujo crítico? | Sí: controla la publicación y el retiro de material educativo del portal estudiantil. |
| ¿Hay entre cinco y diez escenarios? | Sí: siete, con casos válidos, validaciones y desactivación. |
| ¿Las reglas se expresan en lenguaje de negocio? | Sí: guardar, publicar, revisar y desactivar se relacionan con acciones del docente y resultados visibles. |
| ¿Cómo se comprueban los ejemplos? | Cada escenario se vincula con pasos pytest-bdd y acciones o aserciones Selenium. |

El análisis académico queda documentado en los siete escenarios existentes. Si
se modifica una regla del sistema, se actualiza primero su ejemplo en el
`.feature`, después la implementación y finalmente se valida en CI.
