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
