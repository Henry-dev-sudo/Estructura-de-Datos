# Laboratorio Práctico 2: Integración y Aplicación de LIFO, FIFO y Árboles en Python

Este proyecto es una aplicación de consola desarrollada en Python que simula el sistema de gestión de una terminal de transportes. Integra estructuras de datos fundamentales (**Pilas**, **Colas** y **Árboles**) para resolver necesidades operativas reales de la empresa.

Cómo Ejecutar el Código

Para poner en marcha la aplicación, asegúrate de tener instalado **Python** (versión 3.x recomendada). Abre tu terminal o consola en la carpeta del proyecto y ejecuta el siguiente comando:

```
python lab.py

```

Al iniciar, se desplegará un menú interactivo en consola con las diferentes opciones de gestión (registro de pasajeros, control de salidas, visualización de destinos y funciones especiales).

## Estructuras de Datos y Funciones Principales

### 1. Cola de Pasajeros (`FIFO` - First In, First Out)

* **Propósito:** Organizar el orden de llegada de los pasajeros en espera de atención.

* **Funcionamiento:** Los nuevos pasajeros se agregan al final de la estructura mediante `.append()` y se atiende primero al que llegó antes utilizando `.pop(0)`.

* **Validación:** Se verifica que la cola no esté vacía antes de atender.

### 2. Pila de Salidas de Buses (`LIFO` - Last In, First Out)

* **Propósito:** Registrar y controlar las salidas de los buses de la terminal.

* **Funcionamiento:** Cada nueva salida se apila al final con `.append()`. La última salida registrada se puede deshacer o retirar utilizando `.pop()`.

### 3. Árbol de Destinos (`NodoDestino`)

* **Propósito:** Mantener organizada la jerarquía de las regiones y destinos de la terminal (Terminal Central $\rightarrow$ Regiones $\rightarrow$ Ciudades).

* **Funcionamiento:** Se implementa mediante una clase recursiva (`NodoDestino`) que almacena el nombre del destino y una lista de hijos. Cuenta con funciones recursivas para mostrar la jerarquía completa y buscar destinos específicos.

## Mejoras Empresariales Implementadas

Se han seleccionado e implementado dos mejoras clave para optimizar la robustez del sistema:

1. **Evitar Códigos de Bus Duplicados:**

   * *Necesidad que resuelve:* Previene errores humanos y confusiones administrativas al intentar registrar dos salidas con el mismo código de bus.

   * *Implementación:* El sistema recorre la pila de salidas actuales antes de permitir el registro. Si el código ya existe, rechaza la operación y notifica al usuario.

2. **Consultar la Cima de la Pila sin Retirar el Registro (`peek`):**

   * *Necesidad que resuelve:* Permite a la gerencia visualizar cuál fue la última salida registrada de forma inmediata sin alterar ni eliminar el elemento de la estructura.

   * *Implementación:* Evalúa si la pila contiene elementos y muestra la información del último registro accediendo al último índice (`-1`) sin aplicar `.pop()`.

## Métodos Clave de Python Utilizados

Durante el desarrollo del código se utilizaron diversos métodos nativos de Python para asegurar la validación y limpieza de datos:

* **`.strip()`**: Utilizado en las entradas de texto del usuario (como nombres de pasajeros o códigos). Elimina los espacios en blanco sobrantes al principio y al final de la cadena introducida, evitando errores por espacios accidentales.

* **`.append()`**: Empleado tanto en la Pila como en la Cola para insertar nuevos elementos al final de la estructura de lista.

* **`.pop()` y `.pop(0)`**: Utilizados para extraer elementos. `.pop()` retira el último elemento ingresado (LIFO), mientras que `.pop(0)` extrae el primer elemento de la lista (FIFO).