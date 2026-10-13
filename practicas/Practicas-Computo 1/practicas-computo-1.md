# Prácticas de Cómputo 1

Esta carpeta contiene prácticas aplicadas de estructuras de datos en Python. A diferencia de los ejercicios básicos, aquí se construyen pequeños programas para resolver situaciones cercanas a la vida real y justificar la elección de cada estructura.

## Archivos

- [practica1.ipynb](practica1.ipynb): cuaderno de práctica inicial. Puede ampliarse con celdas de explicación, código y resultados.
- [practica2.py](practica2.py): comparación práctica entre listas, tuplas y conjuntos mediante canciones, géneros, cursos aprobados e inventario.
- [practica3.py](practica3.py): aplicación de patrones LIFO/FIFO y conjuntos para verificar requisitos académicos.
- [practica4.py](practica4.py): sistema integral de caja y despacho que combina fila de clientes, bolsas de productos, membresías y cupones.
- [practica05.ipynb](practica05.ipynb): cuaderno de práctica adicional para continuar el trabajo aplicado.
- [../Practicas-Computo 2/practica7.py](../Practicas-Computo 2/practica7.py): ejercicios de matrices con temperaturas y asistencia.
- [../Practicas-Computo 2/Practica8.py](../Practicas-Computo 2/Practica8.py): aplicación de árboles binarios a un catálogo de productos.

## Temas trabajados

### Práctica 1

Se utiliza un notebook como espacio de trabajo para desarrollar ejercicios de forma interactiva, separando código, explicaciones y resultados.

### Práctica 2: listas, tuplas y conjuntos

El archivo `practica2.py` presenta tres casos de uso para comparar las estructuras:

- **Lista de canciones:** se crea una lista mutable con `Rust`, `Wonderwall` y `Everlong`; se recorre con un ciclo `for`, se agrega `I Don't Wanna Be Me` mediante `append()` y se elimina `Rust` mediante `remove()`.
- **Conjunto de géneros:** se crea un `set` con `Aventura`, `Acción`, `RPG` y `Estrategia`. La repetición de `Acción` se descarta automáticamente porque los conjuntos no almacenan duplicados.
- **Tupla de cursos aprobados:** se crea la tupla inmutable `("Matemáticas", "Física", "Química")` para representar información que no debe modificarse.
- **Inventario de productos:** se utiliza otro conjunto con `Laptop`, `Mouse`, `Teclado` y `Monitor`. Las repeticiones de `Laptop` y `Mouse` se eliminan automáticamente y posteriormente se agrega `Auriculares` con `add()`.

La práctica muestra que las listas son adecuadas para colecciones modificables y ordenadas, los conjuntos para evitar duplicados y las tuplas para conservar datos sin cambios.

### Práctica 3: patrones de estructuras

- Uso de LIFO o FIFO para modelar casos de uso cotidianos.
- Conjuntos para verificar requisitos académicos.
- Uso de diccionarios para almacenar materias y calificaciones.
- Comprobación de materias faltantes, materias reprobadas y cumplimiento de requisitos para graduarse.

### Práctica 4: sistema de caja y despacho

- `deque` y `popleft()` para atender clientes en orden de llegada, siguiendo FIFO.
- Listas usadas como pilas para registrar productos en orden LIFO.
- Conjuntos para validar membresías y evitar reutilizar cupones.
- Clases para representar a los clientes y organizar la información de cada compra.
- Condicionales y ciclos para atender la fila, procesar productos y validar casos como una fila vacía.

### Práctica 7: matrices de temperaturas y asistencia

El archivo `practica7.py` trabaja matrices mediante listas anidadas y recorridos con ciclos `for`.

- Se muestra una matriz de temperaturas registradas durante cinco días y tres momentos del día.
- Se calculan promedios por momento del día y promedios por día.
- Se busca la temperatura máxima recorriendo todas las filas y columnas.
- Se muestra una matriz de asistencia donde `1` representa asistencia y `0` inasistencia.
- Se cuentan las asistencias de cada estudiante y el total de estudiantes que asistieron cada día.
- Se identifica al estudiante con mayor cantidad de asistencias.
- El primer ejercicio conserva como referencia comentada un inventario de productos con operaciones de consulta, suma y modificación de una matriz.

### Práctica 8: árbol binario para un catálogo

El archivo `Practica8.py` modela la navegación de un comercio electrónico mediante un árbol binario.

- Se define la clase `Nodo`, con un valor y referencias a los hijos izquierdo y derecho.
- Se crea la raíz `Producto` y se agregan las categorías `Tecnologia` y `Hogar`.
- Se incorporan las subcategorías `Laptops`, `Celulares`, `Cocina` y `Muebles`.
- Se implementa `es_hoja()` para comprobar si una categoría no tiene subcategorías.
- Se muestran la raíz, sus hijos y el resultado de las comprobaciones de hojas.

## Forma de trabajo

Las prácticas se organizan desde la comparación de estructuras básicas hasta la integración de varias estructuras en sistemas completos. Se agregan ejercicios de matrices y árboles binarios para practicar recorridos, cálculos acumulados, búsquedas y clasificación de nodos. Cada archivo incluye comentarios que explican la lógica y la razón de utilizar listas, tuplas, conjuntos, pilas, colas, diccionarios o árboles.
