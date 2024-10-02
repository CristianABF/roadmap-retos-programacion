'''
Operadores
'''

# Operadores aritméticos

print(f"Suma: 5 + 5 = {5 + 5}")
print(f"Resta: 10 - 5 = {10 - 5}")
print(f"Multiplicación: 10 * 5 = {10 * 5}")
print(f"División: 5 * 50 = {5 / 50}")
print(f"Módulo:10 % 3 = {10 % 3}")
print(f"Exponente: 10 ** 5 = {10 ** 5}")
print(f"Módulo: 5 // 50 = {5 // 50}")

# Operadores de comparación

print(f"Igualdad: 5 == 10 es {5 == 10}")
print(f"Desigualdad: 5 != 10 es {5 != 10}")
print(f"Mayor que: 5 > 10 es {5 > 10}")
print(f"Menor que: 5 < 10 es {5 < 10}")
print(f"Mayor o igual que: 5 >= 10 es {5 >= 10}")
print(f"Menor o igual que: 5 <= 10 es {5 <= 10}")

# Operadores lógicos

print(f"AND &&: 10 + 5 == 15 and 5 - 1 == 4 es {10 + 5 == 15 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 15 or 5 - 1 == 4 es {10 + 3 == 15 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignación

my_number = 11 # Asignacón
print (my_number) 
my_number += 1 # Suma y asignación
my_number -= 1 # Resta y asignación
my_number *= 3 # Multiplicación y asignacíon
my_number /= 3 # División y asignación
my_number %= 2 # Módulo y asignación
my_number **= 3 # Exponente y asignación
my_number //= 3 # División entera y asignación
print(my_number)

# Operadores de identidad

my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia

print(f"'u' in 'moure' {'u' in 'moure'}")
print(f"'u' not in 'moure' {'u' not in 'moure'}")

# Operadores de bit
a = 10 # 1010
b = 3 # 0011
print(f"AND: 10 & 3 = {10 & 3}") # 0010
print(f"OR: 10 | 3 = {10 | 3}") # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}") # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}") # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}") # 101000

'''
Estructuras de control
'''

# Condicionales

my_string = "CristianABF"
if my_string == "CristianABF" :
  print("my_string es 'CristianABF'")
elif my_string == "Cristian" :
  print("my_string es 'Cristian'")
else:
  print("my_string no es 'CristianABF' ni 'Cristian'")

# Iterativas

for i in range (11):
  print(i)

i = 0

while i <= 10:
  print(i)
  i += 1

# Manejo de excepciones
try:
  print(10 / 0)
except:
  print("Se ha producido un error")
finally:
  print("Ha finalizado el manejo de excepciones")

"""
Extra
"""

for number in range(10, 56):
  if number % 2 == 0 and number != 16 and number % 3 != 0:
    print(number)
