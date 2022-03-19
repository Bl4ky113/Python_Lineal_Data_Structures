# Platzi Course: Estructuras de Datos Lineales, Python

## Objetivos
- Que son, su importancia y concepto de estructura de datos
- uso de estructura de datos lineales
- practicar lo aprendido

## Elementos de la Programacion en Python

Son varios elementos, partiendo desde:
- Syntaxis:
    como esta escrito como tal python, usando las palabras 
    unicas: while, for, if, else.
- Elementos:
    los elementos basicos de python: str, bool, num y sus posibles 
    operaciones aritmeticas y logicas.
- estructuras de datos:
    Arrays: lists, tuples, dictionaries. Generalmente conocidos como 
    colecciones de datos. Hemos visto una parte de estos, pero solo la 
    punta del iceberg

## Tipo de Collections

Grupo de 0 o mas elementos que se pueden tratar como una unidad principal

### Tipos de elementos:
    - Non-Zero
    - Zero
    - NaN
    - undefined

Hay diferentes tipos de collections, pero los principales son:

Dinamicas: Pueden cambiar sus elementos
Inmutables: No pueden cambiar sus elementos

Algunos de los tipos de collections son, algunas de 
estas tienen diferentes formas de uso, o inclusive representacion y otros.

- Lineales:
    Los valores van en una linea, el primero no tiene predecesor y el ultimo no tiene sucesor a no 
    ser que sea un collection dinamico
- Jerarquicas:
    Los valores van descendiendo en una estructura ramificada, como un arbol. Los elementos cuentan con 
    un padre y puede que tengan hijos e hermanos. Un ejemplo es el sistema de almacenamiento de los OS.
- Grafos:
    Los valores estan interconectados entre si de varias formas, creando nodos, pueden estar conectados 
    todos entre si o que un elemento solo tenga una coneccion. Ej Redes Neuronales y Nodos.
- Desordenadas:
    Los elementos no tienen un orden total o siquiera forma de calisificacion, solo estan ahi
- Ordenados:
    Cada elemento en la collection es mayor al anterior y menor al siguiente, bajo los parametros de organizamiento 
    de la collection.

Los que vamos a usar en el curso son los lineales, y para usarlos vamos a tener que hacer diferentes algoritmos de 
organizacion y busqueda. 

Pero ojo, que al hacer estos algoritmos podemos hacerlos con solo 2 caracteristicas de 3:

- Buenos y efectivos
- Baratos
- Rapidos y Eficienties

Dependiendo de lo que necesitemos, los vamos a tener que usar como herramientas de software y codigo.

## Operaciones de Linear Collections

- Tamano: Obtener el size
- Pertenencia: saber si un elemento pertenece
- recorrido: recorrer la Collection 
- string
- verificar igualdad
- concatenacion
- convertir 
- insertar
- quitar
- reemplazar
- acceder

## Collections integradas en Python

- Lists:
    - [], list()
    - Muy usadas
    - dinamico
    - secuencial, con indices
    - Ordenable
- Tuples:
    - ()
    - inmutable
    - usado en datos constantes
    - son mas rapidas para ser usadas, vs las lists
    - secuencial, con indices
    - ordenable
- Sets:
    - {}
    - no tienen elementos duplicados
    - aun mas rapidos
    - tienen operaciones logicas de grupos
    - son desordenados
- Dictionary:
    - {"key": value}
    - tienen keys y values, siendo asiosiativos
    - son desordenados

## Arrays

Son una estructura en la que se pueden almacenar datos en una collection. 
Esta collection es parecida a las lists de python, y estas disponibles en casi cualquier lenguaje
de programacion.

Los arrays en la parte tecnica de la memoria, son elementos que se les define un espacio en memoria, para poder 
almacenar un numero estatico de elementos. Este numero de elementos, a diferencia de las lists, no se puede 
cambiar agregando o borrando elementos.

En python hay un modulo para crear los arrays, pero estos igualmente estan basados en las lists.

Pero tambien podemos agregar nuestro propio obj con OOP para crear Arrs.

## Arrays 2D

Es un array que ya hemos usado, su estructura es general, como una tabla. Generalmente creada con filas y columnas, 
y con Arrays dentro de otro Array.

Y aprovechando que hemos hecho una clase de Arrays, podemos usarla para hacer otra clase con polymorphism.

## Nodos y Singly linked list

Los nodos son formas de almacenar datos, que tienen referencia a otro Nodo. Al hacer una cadena de nodos 
referenciandose entre si, vamos a obtener una Singly Linked List. Estas listas pueden ser sencillas o dobles.
Y para acceder cada dato vamos a tener que pasar con cada valor hasta llegar al indicado.

Los nodos tienen la estructura:
- Data: Valor almacenado
- Next: Referencia al siguiente nodo, null o None si no hay siguiente nodo
- Previous: Referencia al anterior nodo, null o None si no hay anterior nodo
- Head: Referencia al primer nodo
- Tail: Referencia al ultimo nodo

Estos nodos se guardan en memoria en espacios aleatoreos, teniendo unicamente las referencias a los 
otros nodos como conexion entre si. Esto puede ser muy rapido al momento de hacer optimizacion. Pero debemos
tener en cuenta que se puede volver una coneccion O(n)

Ademas las singly linked list funciona como base para hacer diferentes formas de estructuras como 
las stacks o los queues. 

La diferencia entre listas sencillas y dobles, es que las sencillas solo se pueden recorrer en un sentido. 
Pero las dobles son de alfrente hacia atras. 

Algunos de sus usos comunes son el ctrl+z y ctrl+y. El historial de navegacion en una tab.

### Metodos Y Operaciones

En los diferentes metodos de las Singly Linked List vamos a tener que hacer uso de
variables sustitutas o temporales, esto para no afectar a la lista, si no es lo que necesitamos.

Generalmente esta variable se va a llamar \"prove\"

Algunos de los metodos son:

- Iteracion
- Busqueda, con y sin index
- Append, con y sin index
- Delete con y sin index
- Replace 
