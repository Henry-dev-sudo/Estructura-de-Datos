# Cuadernillo 3

Este cuadernillo reúne ejercicios de programación en Python y estructuras de datos. Los ejemplos trabajan funciones, estructuras de control, pilas, colas, nodos y árboles binarios mediante programas independientes y pequeños sistemas interactivos.

## Cambios realizados

- Se reorganizaron los archivos de las clases para separar cada tema en carpetas más descriptivas.
- Los ejemplos de funciones y pilas que estaban agrupados en la clase 16 ahora se encuentran en `clase15`, dentro de las carpetas `Funciones` y `Pilas-funciones con Pila`.
- Los ejercicios de condicionales y ciclos ahora están agrupados en `clase 17/Bucles`.
- Los ejercicios de colas se concentraron en `clase 17/Implementación de colas(FIFO)`.
- Se agregaron ejercicios de nodos en `clase18`, árboles binarios en `clase19` y una tarea independiente en `Tareas`.
- Se actualizaron los enlaces de este documento para apuntar a las nuevas ubicaciones de los archivos.

## Estructura de carpetas

### Clases

Los ejemplos están organizados por número de clase y, cuando corresponde, por tema:

- `clase15/Funciones`: funciones básicas.
- `clase15/Pilas-funciones con Pila`: implementación de pilas con listas y funciones.
- `clase 17/Bucles`: estructuras condicionales y ciclos.
- `clase 17/Implementación de colas(FIFO)`: implementación de colas y un sistema de turnos.
- `clase18`: creación y uso de nodos.
- `clase19`: árboles binarios y recorridos recursivos.

### Tareas

La carpeta `Tareas` contiene ejercicios prácticos independientes de las clases, como el sistema de aceleración y desaceleración de un vehículo.

## Temas trabajados

### Clase 15: funciones y pilas

#### Funciones

- [funciones.py](Clases/clase15/Funciones/funciones.py): definición de funciones, parámetros, valores de retorno y funciones para saludar o sumar.

#### Pilas

- [pilas.py](<Clases/clase15/Pilas-funciones con Pila/pilas.py>): representación de una pila mediante una lista y uso de `append()` para agregar elementos.
- [funcionesPila.py](<Clases/clase15/Pilas-funciones con Pila/funcionesPila.py>): creación de las operaciones `push` y `pop` para agregar y retirar elementos siguiendo el principio LIFO.

La separación de estos archivos permite distinguir la creación de una pila de las funciones que controlan sus operaciones. La lista se utiliza como almacenamiento y el último elemento agregado es el primero en retirarse.

### Clase 17: estructuras de control y colas

#### Bucles y condicionales

- [if.py](<Clases/clase 17/Bucles/if.py>): toma de decisiones con `if` y `else`.
- [Elif.py](<Clases/clase 17/Bucles/Elif.py>): evaluación de varias condiciones con `if`, `elif` y `else`.
- [for.py](<Clases/clase 17/Bucles/for.py>): repetición de instrucciones con el ciclo `for` y `range()`.
- [while.py](<Clases/clase 17/Bucles/while.py>): repetición controlada con el ciclo `while`.

#### Colas FIFO

- [cola.py](<Clases/clase 17/Implementación de colas(FIFO)/cola.py>): creación de una cola con listas y agregación de elementos.
- [Operaciones-de-cola.py](<Clases/clase 17/Implementación de colas(FIFO)/Operaciones-de-cola.py>): operaciones `enqueue`, `peek`, `size`, `dequeue`, `rear` e identificación de una cola vacía.
- [sistema-de-un-banco.py](<Clases/clase 17/Implementación de colas(FIFO)/sistema-de-un-banco.py>): sistema de turnos bancarios con registro de clientes, consulta del siguiente turno, atención y visualización de la cola.

En estos ejercicios se muestra la diferencia entre agregar un elemento al final de una cola y retirar el elemento del frente. El sistema bancario aplica FIFO para atender a los clientes en el mismo orden en que llegan.

### Clase 18: nodos

- [nodos.py](Clases/clase18/nodos.py): definición de la clase `Nodo` con un valor y referencias izquierda y derecha. El archivo construye un árbol genealógico, un menú de decisiones y una jerarquía de carpetas; además incluye recorridos en preorden y postorden, conteo de nodos, conteo de hojas y búsqueda de valores.

### Clase 19: árboles binarios

- [ArbolesBinarios.py](Clases/clase19/ArbolesBinarios.py): construcción de un árbol binario con diez nodos numéricos, relaciones izquierda-derecha, recorrido en preorden, conteo recursivo de nodos y cálculo de la altura.

También se incorporan comprobaciones para identificar si un nodo es hoja, es decir, si no tiene hijos. Estas comprobaciones se aplican a un catálogo de productos con las categorías `Tecnologia`, `Hogar`, `Laptops`, `Celulares`, `Cocina` y `Muebles`.

## Tareas

- [Sistema-Aceleracion-Desaseleración.py](Tareas/Sistema-Aceleracion-Desaseleración.py): uso de las funciones `acelerar()` y `desacelerar()` para aumentar o disminuir la velocidad de un vehículo en 10 km/h.

La tarea solicita una velocidad inicial, aplica la función `acelerar()` para incrementarla en 10 km/h y después utiliza `desacelerar()` para reducirla en 10 km/h, mostrando ambos resultados.