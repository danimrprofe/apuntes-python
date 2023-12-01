
# Manejo de Errores en Python

En Python, hay dos tipos de errores que los programadores pueden encontrar: errores de sintaxis y excepciones.

## Errores de Sintaxis

Los errores de sintaxis ocurren cuando olvidas un símbolo o escribes algo mal, como olvidar dos puntos al final de una línea o cometer un error de ortografía en una palabra clave. Estos errores se muestran inmediatamente cuando intentas ejecutar el código y se conocen como errores de sintaxis.

## Excepciones

Las excepciones ocurren cuando hay un error en el código, pero no se produce un error de sintaxis. Por ejemplo, una excepción puede ocurrir si intentas dividir un número entre cero, ya que esto no está permitido en Python. En este caso, Python mostrará un mensaje de error especial que describe la excepción.

## Try and Except

En Python, hay una forma de manejar excepciones usando la sentencia try and except. La sentencia try and except le permite a los programadores "capturar" excepciones que ocurren en su código y proporcionar una respuesta adecuada.

Aquí hay un ejemplo de cómo se usa la sentencia try and except:

```python
try:
   # intenta ejecutar este código
   result = 10 / 0
except ZeroDivisionError:
   # si hay una excepción, se ejecuta este código
   print("No se puede dividir entre cero")
```

En este ejemplo, la sentencia try intenta ejecutar el código dentro de ella. Si hay una excepción, se salta la sentencia try y se ejecuta la sentencia except, que muestra un mensaje de error.

## Finally

En algunos casos, puede que desees que una parte de tu código se ejecute independientemente de si hay una excepción o no. Para esto, puedes usar la sentencia finally. La sentencia finally se ejecutará siempre, incluso si hay una excepción.

Aquí hay un ejemplo de cómo se usa la sentencia finally:

```python
try:
   # intenta ejecutar este código
   result = 10 / 0
except ZeroDivisionError:
   # si hay una excepción, se ejecuta este código
   print("No se puede dividir entre cero")
finally:
   # esta sentencia se ejecutará siempre
   print("Esta sentencia se ejecutará siempre")
``