# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
print(palabra_1[0], palabra_1[1])
parte_1 =palabra_1[0]+ palabra_1[1]
# De la segunda palabra tome las primeras dos letras, utilice el operador :
print(palabra_2[0], palabra_2[1])
parte_2 =palabra_2[0]+ palabra_2[1]
# Formar una nueva palabra con los recortes solicitados
nueva_palabta= parte_1 + parte_2
# Imprima en pantalla los resultados
print(nueva_palabta)