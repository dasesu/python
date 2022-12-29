Notas muy rapidas o interesantes sobre python
===

Python no usa punto y coma `;` para terminar una declaracion
Pero se puede usar el punto y coma `;` para tener dos sentencias en la misma línea.
```py
x = 5; y = 10  # esto es valido.
```

Haciendo uso de `\` se puede romper el código en varias líneas, hace que el código sea mucho más legible.
```py
x = 1 + 2 + 3 + 4 +\
    5 + 6 + 7 + 8
```

Si estamos dentro de un bloque rodeado con paréntesis (), bastaría con saltar a la siguiente línea.
```py
x = (1 + 2 + 3 + 4 +
     5 + 6 + 7 + 8)
```

Los comentarios de una linea se hacen con #
Comentarios de varias lineas comienzan por ''' y terminan por ''' o """ y """ respectivamente 

para imprimir por pantalla se usa la funcion print.
```py
print ("Hola mundo")
```

asignacion de variables no lleva un tipo asignado
```py
x = 5
```


Podemos por ejemplo asignar el mismo valor a diferentes variables con el siguiente código.
```py
x = y = z = 10  # a todas asigna 10
```

O tambien podemos asignar valores simultaneamente asi:
```py
x, y, z = 1, 2, 3 # Asigna los valores a sus respectivas posiciones
```

Cuando imprimimos variables separadas por comas python las separa con un espacio " "
```py
name = "Sebastian"
surname = "Suarez"
print (name, surname) # imprime: Sebastian Suarez
```

Python es Case sensitive.

for loop
se parece mucho al for en C++, podria leerse como va a comenzar en 1 y va a continuar mientras no el valor sea distinto de 10, la cual es la condicion de parada

```
for i in range(1,10):
    print(i) # print 1 2 3 4 5 6 7 8 9, no llega a 10
```
El equivalente en while podria verse asi
```
x = 1
while x < 10:
    print(x)
    x += 1
```

Tiene la opcion de indicar de cuanto en cuanto iterar, nuevamente se parece a C++ en esto, que seria como agregar en el ultimo campo, un i+2
```
for i in range(1,10,2):
    print(i)
```

Recorre el string word
```
for i in word:
    print(i)
```

Random:
```py
import random # carga el modulo random
num = random.random() # crea un numero aleatorio entre 0 y 1
num = num * 100 # si quiero un numero aleatorio entre 0 y 100
print(num)
```

Selects a random whole number between 0 and 9 (inclusive).
```
num = random.randint(0,9)
```

Picks a random number between the numbers 0 and 100 (inclusive) in steps of five
```
num = random.randrange(0,100,5)
```

random from options
```
colour = random.choice([“red”,“black”,“green”])
```

Turtle:
importa la libreria turtle para su uso
```
import turtle
```
Defines the window as being called “scr”
```
scr = turtle.Screen()
```

Sets the screen background colour to yellow
scr.bgcolor(“yellow”)

Removes the pen from the page
turtle.penup()

Places the pen on the page so that when the turtle moves it will leave a trail behind it.
By default, the pen is down unless specified otherwise.
turtle.pendown()

Changes the turtle pen size
turtle.pensize(3)

Turns the turtle 120° to the left
turtle.left(120)

Turns the turtle 90° to the right (clockwise)
turtle.right(90)

Moves the turtle forward 50 steps.
turtle.forward(50)

Changes the shape of the turtle to look like a turtle
turtle.shape(“turtle”)

Hides the turtle so it is not showing on the screen.
turtle.hideturtle()


Shows the turtle on the screen.By default, the turtle is showing unless specified otherwise.
turtle.showturtle()

Entered before the code that draws a shape so it knows to fill in the shape it is drawing.
turtle.begin_fill()


Entered after the code that is drawing the shape to tell Python to stop filling in the shape.
turtle.end_fill()

Defines the colours filling in the shape. This example will make the shape have a black outline and a red fill. This needs to be entered before the  shape is drawn.
turtle.color(“black”,“red”)

When the user clicks on the turtle window
turtle.exitonclick()

'''''''''''''''''''''''''''
El uso de global funciona como crear una variable static, cuando es local la puede hacer global
```py
a = 0

def suma_uno():
    global a
    a = a + 1

suma_uno()
print(a)
```

El uso de nonlocal es útil cuando tenemos funciones anidadas, la x dentro de funcion_b modifica el valor de x en funcion_a
```py
def funcion_a():
    x = 10

    def funcion_b():
        nonlocal x
        x = 20
        print("funcion_b", x)

    funcion_b()
    print("funcion_a", x)
```

Pertenencia e Identidad: in, is

El uso de `in` nos permite saber si un determinado elemento está en una clase iterable, devolviendo True en el caso de que sea cierto.
```py
lista = ["a", "b", "c"]
print("a" in lista)

# Salida: True
```

El uso de is nos permite saber si dos variables apuntan en realidad al mismo objeto. Por debajo se usa la función id()

El uso de `del` nos permite eliminar una variable del scope,
```py
a = 10
del a
print(a)
```


Iterables en python:
```py
from collections import Iterable
lista = [1, 2, 3, 4]
cadena = "Python"
print(isinstance(lista, Iterable)) ''' Retorna true cuando lista es de tipo iterable.
```

Para entender los iteradores, es importante conocer la función iter() y next().
`it` es un iterador, de la clase list_iterator, Esta variable iteradora, hace referencia a la lista original y nos permite acceder a sus elementos con la función next(). Cada vez que llamamos a next() sobre it, nos devuelve el siguiente elemento de la lista original

Lamentablemente no existe ninguna opción de volver al elemento anterior.

```py
lista = [5, 6, 3, 2]
it = iter(lista)
print(next(it))
#     [5, 6, 3, 2]
#      ^
#      |
#     it
print(next(it))
#     [5, 6, 3, 2]
#         ^
#         |
#        it
print(next(it))
#     [5, 6, 3, 2]
#            ^
#            |
#           it
```
Para saber mas: Existen otros iteradores para diferentes clases:

    str_iterator para cadenas
    list_iterator para sets.
    tuple_iterator para tuplas.
    set_iterator para sets.
    dict_keyiterator para diccionarios.


iterando cadena al revés. Haciendo uso de [::-1] se puede iterar la lista desde el último al primer elemento.
```py
texto = "Python"
for i in texto[::-1]:
    print(i) #n,o,h,t,y,P
```


Itera la cadena saltándose elementos. Con [::2] vamos tomando un elemento si y otro no.
```py
texto = "Python"
for i in texto[::2]:
    print(i) #P,t,o
```

