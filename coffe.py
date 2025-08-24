eleccionValida = False
print("""
Bienvenido A la Cafetería
Tenemos los siguientes tipos de café: espresso, latte, cappuccino
¿Qué tipo de café te gustaría?
""")
while not eleccionValida:
    eleccion = input("Elige un tipo de café (espresso, latte, cappuccino): ").lower()
    for i in ["espresso", "latte", "cappuccino"]:
        if eleccion == i:
            print(f"Has elegido {eleccion}.")
            eleccionValida = True
            break
    if not eleccionValida:
        print("Elección inválida. Por favor, elige entre espresso, latte o cappuccino.")