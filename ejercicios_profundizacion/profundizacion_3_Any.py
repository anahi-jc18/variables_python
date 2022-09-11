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

# Ejercicios de práctica con cadenas
'''
Enunciado:
Realice un programa que reciba por consola su nombre completo
e imprima en pantalla su nombre en los siguientes formatos:
- Todas las letras en minúsculas
- Todas las letras en mayúsculas
- Solo la primera letra del nombre en mayúscula

NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
de strings:
- lower
- upper
- capitalize

Puede buscar en internet como usar en Python estos métodos.
Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

Link de referencia:
https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

Cualquier duda con estos métodos pueden consultarla por el campus
'''

print('Ahora si! buena suerte')
# Empezar aquí la resolución del ejercicio

print("Ingrese su nombre completo")
name = str(input())

print("Nombre completo:", name.lower())
print("Nombre completo:", name.upper())
print("Nombre completo:", name.capitalize())



#En la linea 47 al ingresar mi nombre completo(Anahi jimena cano), me transformaba solo la primer letra. Con el ejercicio 4 de profundizacion
#tome el comando split que podria aplicarlo en este punto para transformar las iniciales del nombre en mayuscula, pero no funciona.

print("Nombre completo:", name.capitalize().split(' ')[0],name.capitalize().split(' ')[1],name.capitalize().split(' ')[2])

