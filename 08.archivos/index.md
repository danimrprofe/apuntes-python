# Archivos

## Leer un archivo

Para leer un archivo primero necesitamos abrirlo en modo lectura, usando la función `open()`:

```python
f = open("archivo.txt", "r")
```

Ahora podemos leer el archivo usando la función `read()`:

```python
text = f.read()
```

Finalmente, es importante recordar cerrar el archivo usando la función `close()`:

```python
f.close()
```

Si utilizamos “r”, abrimos el archivo en modo lectura.

```python
with open('texto.txt', 'r') as archivo:
    texto = archivo.read()
    print(texto)
```

## Leer línea por línea

También podemos ir leyendo línea por línea

```python
# Abrir el archivo
archivo = open("archivo.txt", "r")

# Leer cada línea
for linea in archivo:
    print(linea)

# Cerramos el archivo
archivo.close()
```

## Eliminar un archivo

Para borrar un archivo podemos utilizar la librería os. Para ello, al principio de nuestro archivo debemos importarla.

```python
# Eliminar un archivo llamado "test.txt"
import os
os.remove("archivo.txt")
```

Actividad: Crea un programa que te pida el nombre, tu peso y tu edad, y calcule tu índice de masa corporal (busca la fórmula). A continuación, deberá guardar esta información en una línea nueva en un archivo nuevo.

## Escribir en un archivo

Para escribir en un archivo primero necesitamos abrirlo en modo escritura, usando la función `open()`:

```python
f = open("archivo.txt", "w")
```

Ahora podemos escribir en el archivo usando la función `write()`:

```python
f.write("Esto se escribirá en el archivo")
```

Finalmente, es importante recordar cerrar el archivo usando la función `close()`:

```python
f.close()
```

Ejemplo:

```python
with open('texto.txt', 'w') as archivo:
    archivo.write("Esta es la línea 1\n")
    archivo.write("Esta es la línea 2\n")
    archivo.write("Esta es la línea 3\n")
```

## Agregar información a un archivo

```python
# abrir el archivo
with open('archivo.txt', 'a') as archivo:
    # escribir una línea
    archivo.write('Esta es una línea de texto añadida al archivo')
```