# Función de validación
def funcion_de_validacion(valor_a_buscar, lista_de_valores):
    if valor_a_buscar in lista_de_valores:
        return True
    else:
        print("ERROR: Select something from the menu")
        return False


Total = 0

print("           CHOOSE A DRINK")
print("1.Capuccino $3.00   2.Espresso $2.50")
print("3.Macchiato $2.50   4.Americano $3.00")
print("5.Mocha $3.50       6.Latte $2.50")
print("7.Flat White $2.50")

drinks = [3.00, 2.50, 2.50, 3.00, 3.50, 2.50, 2.50]

# --- Selección de bebida ---
opcion = int(input("         ENTER THE NUMBER: "))
while not funcion_de_validacion(opcion, list(range(1, 8))):
    opcion = int(input("choose a coffee:"))

Total += drinks[opcion - 1]


# --- Selección de tamaño ---
print("PICK A SIZE")
print("1. Medium $0.00")
print("2. Large +$1.00")
print("3. XL +$1.50")

sizes = [0.00, 1.00, 1.50]

opcion2 = int(input("         ENTER THE NUMBER: "))
while not funcion_de_validacion(opcion2, list(range(1, 4))):
    opcion2 = int(input("choose a size:"))

Total += sizes[opcion2 - 1]


# --- Selección del lugar ---
print("Eat in or take away?")
print("1. Eat-in $0.00")
print("2. Take away +$1.00")

places = [0.00, 1.00]

opcion3 = int(input("         ENTER THE NUMBER: "))
while not funcion_de_validacion(opcion3, list(range(1, 3))):
    opcion3 = int(input("choose the place where you will consume:"))

Total += places[opcion3 - 1]


# --- Resultado final ---
print(f"Total to pay: ${Total:.2f}")
print("Have a nice day :)")