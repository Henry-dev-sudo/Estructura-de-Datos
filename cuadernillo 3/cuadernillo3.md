# Cuadernillo 3

Este cuadernillo reúne ejercicios de programación en Python y estructuras de datos. Los ejemplos trabajan funciones, estructuras de control, pilas, colas, nodos y árboles binarios mediante programas independientes y pequeños sistemas interactivos.

**Lenguaje:** Python 3.x · **Modalidad:** individual

## Cómo ejecutar el código

1. Instala Python 3.x y abre una terminal en la carpeta del proyecto.
2. Ejecuta cualquier archivo con `python ruta/al/archivo.py`. Ejemplo: `python "Clases/clase15/Pilas-funciones con Pila/funcionesPila.py"`.
3. Los archivos `sistema-de-un-banco.py` y `Sistema-Aceleracion-Desaseleración.py` son interactivos: piden datos por teclado.
4. `funciones.py` y `pilas.py` contienen ejemplos comentados: para ver su salida hay que quitar el `#` de las líneas que se quieran probar.
5. Los demás archivos imprimen su resultado directamente.

## Estructura de carpetas

```
Clases/
├── clase15/
│   ├── Funciones/funciones.py
│   └── Pilas-funciones con Pila/  (pilas.py, funcionesPila.py)
├── clase 17/
│   ├── Bucles/                    (if.py, Elif.py, for.py, while.py)
│   └── Implementación de colas(FIFO)/  (cola.py, Operaciones-de-cola.py, sistema-de-un-banco.py)
├── clase18/nodos.py
├── clase19/ArbolesBinarios.py
└── clase 20/OpArbolesBn.py
Tareas/Sistema-Aceleracion-Desaseleración.py
```

## Temas trabajados

### Clase 15: funciones y pilas (LIFO)

- [funciones.py](Clases/clase15/Funciones/funciones.py): tres ejercicios sobre funciones, dejados como comentarios: saludar sin parámetros, sumar dos números con `return` y saludar a dos nombres ingresados por teclado.
- [pilas.py](<Clases/clase15/Pilas-funciones con Pila/pilas.py>): creación de una pila vacía con una lista. Incluye, comentado, un ejemplo de agregado de los elementos A, B, C, D y E con `append()`.
- [funcionesPila.py](<Clases/clase15/Pilas-funciones con Pila/funcionesPila.py>): operaciones `push` y `pop` como funciones. Agrega A, B y C a la pila, la muestra y retira el último elemento (C).

En una pila el último elemento agregado es el primero en retirarse (Last In, First Out).

### Clase 17: estructuras de control y colas (FIFO)

#### Bucles y condicionales

- [if.py](<Clases/clase 17/Bucles/if.py>): decisión con `if` y `else` para saber si una persona es mayor o menor de edad.
- [Elif.py](<Clases/clase 17/Bucles/Elif.py>): clasificación de una nota con `if`, `elif` y `else` (Excelente, Aprobado, insuficiencia o Reprobado).
- [for.py](<Clases/clase 17/Bucles/for.py>): repetición con `for` y `range()`; incluye, comentado, el recorrido de una lista de clientes.
- [while.py](<Clases/clase 17/Bucles/while.py>): repetición controlada con `while`, contando del 1 al 5.

#### Colas

- [cola.py](<Clases/clase 17/Implementación de colas(FIFO)/cola.py>): creación de una cola con una lista, agregado de tres nombres con `append()` y muestra de la cola.
- [Operaciones-de-cola.py](<Clases/clase 17/Implementación de colas(FIFO)/Operaciones-de-cola.py>): ejemplo de la tienda Rosita con las operaciones `enqueue` (`append`), `peek`, `size` (`len`), `dequeue` (`pop(0)`), `rear` e `is empty`.
- [sistema-de-un-banco.py](<Clases/clase 17/Implementación de colas(FIFO)/sistema-de-un-banco.py>): sistema de turnos del "Banco de Manguitos" con menú: registrar cliente (turno con formato `T001`, `T002`...), ver siguiente, llamar al cliente, mostrar todos los clientes y salir.

En una cola se agrega al final y se retira del frente (First In, First Out). El banco atiende en el orden de llegada.

### Clase 18: nodos

- [nodos.py](Clases/clase18/nodos.py): clase `Nodo` con valor y referencias izquierda y derecha. Construye un árbol de 10 nodos numéricos y aplica recorrido en **preorden**, conteo recursivo de nodos y cálculo de la **altura**.

### Clase 19: árboles binarios

- [ArbolesBinarios.py](Clases/clase19/ArbolesBinarios.py): caso práctico del catálogo de e-commerce "NovaMart". Árbol con la raíz `Producto`, las categorías `Tecnologia` y `Hogar`, y las subcategorías `Laptops`, `Celulares`, `Cocina` y `Muebles`. Incluye la función `es_hoja()` para saber si un nodo no tiene hijos.

### Clase 20: árbol binario de búsqueda (BST)

- [OpArbolesBn.py](<Clases/clase 20/OpArbolesBn.py>): **árbol binario de búsqueda (BST)** para un inventario de productos (código, nombre, cantidad). Implementa `agregar` (sin duplicados), `buscar`, `actualizar`, `eliminar` (sin hijos, un hijo y dos hijos con sucesor) y recorrido **inorden**, que muestra los códigos ordenados.

## Tareas

- [Sistema-Aceleracion-Desaseleración.py](Tareas/Sistema-Aceleracion-Desaseleración.py): pide una velocidad inicial (si es negativa la toma como 0), usa `acelerar()` para sumar 10 km/h y `desacelerar()` para restar 10 km/h sin bajar de 0, mostrando ambos resultados.
