Feature: Publicación controlada de material educativo
  Como docente de LENSEGUA
  Quiero preparar y publicar material visual validado
  Para que los estudiantes consulten únicamente contenidos completos y autorizados

  Scenario: Guardar un contenido como borrador
    Given que estoy en la gestión de contenidos de LENSEGUA
    When ingreso el título "La vocal A"
    And presiono el botón "Guardar borrador"
    Then debería ver el mensaje "Contenido guardado como borrador"
    And el contenido debería tener el estado "Borrador"
    And el contenido no debería aparecer en el portal estudiantil

  Scenario: Publicar un contenido completo y revisado
    Given que estoy en la gestión de contenidos de LENSEGUA
    When selecciono el módulo "Vocales"
    And ingreso el título "La vocal A"
    And ingreso el recurso "https://lensegua.local/vocal-a.mp4"
    And confirmo que el material fue revisado
    And presiono el botón "Publicar contenido"
    Then debería ver el mensaje "Contenido publicado correctamente"
    And el contenido debería tener el estado "Publicado"
    And debería aparecer "La vocal A" en el portal estudiantil

  Scenario: Impedir la publicación sin seleccionar módulo
    Given que estoy en la gestión de contenidos de LENSEGUA
    When ingreso el título "Número uno"
    And ingreso el recurso "https://lensegua.local/numero-uno.png"
    And confirmo que el material fue revisado
    And presiono el botón "Publicar contenido"
    Then debería ver el mensaje "Debe seleccionar un módulo"
    And el contenido no debería aparecer en el portal estudiantil

  Scenario: Impedir la publicación sin título
    Given que estoy en la gestión de contenidos de LENSEGUA
    When selecciono el módulo "Números"
    And ingreso el recurso "https://lensegua.local/numero-dos.png"
    And confirmo que el material fue revisado
    And presiono el botón "Publicar contenido"
    Then debería ver el mensaje "El título es obligatorio"
    And el contenido no debería aparecer en el portal estudiantil

  Scenario: Impedir la publicación sin recurso multimedia
    Given que estoy en la gestión de contenidos de LENSEGUA
    When selecciono el módulo "Colores"
    And ingreso el título "Color azul"
    And confirmo que el material fue revisado
    And presiono el botón "Publicar contenido"
    Then debería ver el mensaje "El recurso multimedia es obligatorio"
    And el contenido no debería aparecer en el portal estudiantil

  Scenario: Impedir la publicación de material no revisado
    Given que estoy en la gestión de contenidos de LENSEGUA
    When selecciono el módulo "Abecedario"
    And ingreso el título "Letra B"
    And ingreso el recurso "https://lensegua.local/letra-b.mp4"
    And presiono el botón "Publicar contenido"
    Then debería ver el mensaje "Debe confirmar que el material fue revisado"
    And el contenido no debería aparecer en el portal estudiantil

  Scenario: Desactivar un contenido publicado
    Given que existe un contenido publicado titulado "Color verde" en el módulo "Colores"
    When presiono el botón "Desactivar contenido"
    Then debería ver el mensaje "Contenido desactivado correctamente"
    And el contenido debería tener el estado "Inactivo"
    And el contenido no debería aparecer en el portal estudiantil
