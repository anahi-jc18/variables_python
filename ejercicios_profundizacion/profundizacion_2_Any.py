# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica numérica y cadenas
'''
Enunciado:
Realice un programa que consulte por consola:
- El nombre completo de la persona
- El DNI de la persona
- La edad de la persona
- La altura de la persona

Finalmente el programa debe imprimir dos líneas de texto por separado
- En una línea imprimir el nombre completo y el DNI, aclarando de que
  campo se trata cada uno
        Ej: Nombre Completo: Nombre Apellido , DNI:35205070,
- En la segunda línea se debe imprimir el nombre completo, edad y
  altura de la persona
  Nuevamente debe aclarar el campo de cada uno, para el que lo lea
  entienda de que se está hablando.
'''

print('Sistema de ingreso de datos')
# Empezar aquí la resolución del ejercicioa

print("Ingrese su nombre completo")
name = str(input())
print("Nombre completo:", name)

print("Ingrese su numero de dni sin puntos ni comas")
dni = int(input())
print("Numero de Dni:", dni)

print("Ingrese su edad")
age = int(input())
print("Nombre completo:", age)

print("Ingrese su altura en cm puede ser numero entero o dividido con punto")
high = float(input())
print("Nombre completo:", high)

"""
Consulta: En el punto de altura, el usuario solo puede ingresar su altura con numero entero por ejemplo 151 o 1.51. 
Si el usuario decide dividir su altura con una comma el comando se rompe. 
Cual es la solucion correcta? Indicarle al usuario los valores que toma el comando o pasarlo a str
GRACIAS!!!!
Anahi
