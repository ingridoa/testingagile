=============================== 
Grupo N°10 - Integrantes: Ingrid Oñate - Gabriel Balbontin - Victor Diaz

Modulo :  M4-Testing en un entorno ágil / Reservas
==============================

#### Preguntas Finales

### ¿En qué se diferencia Agile Testing del enfoque tradicional?

     Agile Testing se integra desde el inicio del desarrollo y forma parte del ciclo iterativo e incremental. En cambio, el enfoque tradicional (waterfall) suele dejar las pruebas para el final del proceso.
  
### ¿Qué ventajas viste al usar TDD? ¿Qué te costó más?
  
    Obliga a pensar primero en el comportamiento esperado del código.
    El código resultante suele ser más limpio y modular.
    Previene errores tempranos y mejora la cobertura de pruebas.
    Mayor confianza al refactorizar.

- Lo más difícil:

    Cambiar el hábito de “codificar primero y probar después”.
    Al principio, puede parecer más lento.
    Diseñar buenas pruebas sin haber implementado el código aún.

### ¿Qué tipo de prueba crees que más valor aportó hoy?

    Simulan el comportamiento real del usuario.
    Detectan conflictos de lógica (por ejemplo, reservas duplicadas).
    Verifican que múltiples componentes del sistema trabajen bien juntos (API, lógica, estado).


### ¿Cómo mantendrías esta suite de pruebas con el tiempo?
  
   Organizando el código de prueba: Usar nombres claros, separar unitarias de integración.
   Revisándola con cada cambio de funcionalidad: Actualizar o añadir pruebas al modificar requisitos.
   Documentando casos relevantes: Explicar por qué existe cada prueba crítica.
   Eliminando pruebas obsoletas: Si ya no representan el comportamiento esperado