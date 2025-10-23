print("Hola Mundo")

#Identificadores
# 1.- No inicien con números
# 2.- Sean claros y explicativos
num_1 = 1
num_2 = 2
# 3.- Notación:
#       Camel Case:
#           diasDelMes
#       Snake Case:
#           dias_del_mes

# Constantes
API_KEY = "JKAWJSAJKDASD"

# Tipos De Datos
# int: 1, 2, 3, 0
# float: 1.2, 2.924424, 0.252543
# complex: 3 + 2j (Numeros Imaginarios)
# str: "a", "-", 'hola mundo'
# bool: True o False
# list: ["hola", "mundo"], [1, 2, 4, 5], [1, 2, 3, 0.9, .92], [[1,2, ["a", "b"]], []]
lista_nombres = ["nombre1", "nombre2"]
# dict: {"luis": "662432324243", "adrian": "562543342"}
# { [1,2,3]: {"a":12} }

# Operadores Lógicos
# >, <, >=, <=, ==, not
a = 1
resultado = (bool(a != 1))
print(a < 1) # 1 es menor que 1?
print(a > -2) # 1 es mayor que -2?
print(a >= 1) # 1 es mayor o igual que 1?
print(a <= 2) # 1 es menor o igual que 2?
print(a == 1) # a es 1?
print(f"1 es distinto de 1?? {resultado}") # 1 es distinto de 1?
print(f"Y 1 es distinto de -1?? {not resultado}") # 1 es distinto de -1?

num1 = [1,2,"aa"]
print(num1)
print(type(num1))

# if
b = 8
if b == 10:
    print("Es 10!")
else:
    print("No es 10 xd")

# Ciclos: while, for
c = 3
while c >= 0:
    print(f"Vamos en el: {b}")
    c = c-1

#Uso de la Documentación
num1 = input('dame un numero: ')
num2 = input('dame otro numero: ')
print(type(num1))
# Variables constantes, pueden no ser constantes

print(f"Primero numero: {num1}")
print(f"Segundo Numero: {num2}")

# Convertir la salida de Str a Int
num1_numeric = int(num1)
# Identificador de tipo de salida
print(type(num1))
print(type(num1_numeric))
num2_numeric = int(num2)

# Otro tipo de programacion es que lo ejecute de adentro hacia afuera
# Variable de ejemplo
print(f"Suma: { num1_numeric + num2_numeric}")
print(f"Resta: { num1_numeric - num2_numeric}")