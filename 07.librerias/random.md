# Random

El módulo `random` en Python es un paquete estándar de Python que proporciona varias herramientas para generar números aleatorios. Esta herramienta es útil para todos aquellos programadores que deseen generar números aleatorios en sus proyectos.

## Importando el módulo

Para usar el módulo `random`, primero debe importarlo en su código. Esto se hace escribiendo la siguiente línea de código:

```python
import random
```

## Generando un número aleatorio

Para generar un número aleatorio, primero debe escribir la función `random.randint()`. Esta función recibe dos parámetros: el primer parámetro es el número mínimo que el número aleatorio puede tomar, y el segundo parámetro es el número máximo que el número aleatorio puede tomar.

Por ejemplo, para generar un número aleatorio entre 1 y 10, escriba el siguiente código:

```python
num = random.randint(1, 10)
```

## Generando una lista de números aleatorios

Para generar una lista de números aleatorios, primero debe escribir la función `random.sample()`. Esta función recibe dos parámetros: el primer parámetro es la lista de números que contendrá los números aleatorios, y el segundo parámetro es el número de números aleatorios que desea generar.

Por ejemplo, para generar una lista de 5 números aleatorios entre 1 y 10, escriba el siguiente código:

```python
lista = random.sample(range(1, 11), 5)
```

## Generando una lista de números aleatorios sin repetición

Para generar una lista de números aleatorios sin repetición, primero debe escribir la función `random.shuffle()`. Esta función recibe un parámetro que es una lista de números, y mezcla los elementos de la lista de forma aleatoria.

Por ejemplo, para generar una lista de 5 números aleatorios entre 1 y 10 sin repetición, escriba el siguiente código:

```python
lista = list(range(1, 11))
random.shuffle(lista)
lista = lista[:5]
```