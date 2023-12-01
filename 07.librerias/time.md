# Time


El módulo time de Python proporciona muchas funcionalidades relacionadas con el tiempo como obtener la hora actual, convertir la hora a un formato dado, etc. A continuación, se detallan algunas de las funciones más comunes del módulo time con algunos ejemplos.

### Obtener la hora actual en segundos desde la época

La función `time()` devuelve el número de segundos desde la época (1 de enero de 1970) hasta la hora actual.

```python
import time

# Obtener la hora actual en segundos desde la época
tiempo_actual = time.time()
print("La hora actual en segundos desde la época es:", tiempo_actual)
```

### Obtener la hora actual en un formato determinado

La función `strftime()` se utiliza para convertir la hora a un formato determinado.

```python
import time

# Obtener la hora actual en el formato "%H:%M:%S"
tiempo_actual = time.strftime("%H:%M:%S")
print("La hora actual es:", tiempo_actual)
```