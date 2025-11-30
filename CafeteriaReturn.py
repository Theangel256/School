def validar_opcion(elemento, lista):
    for item in lista:
        if elemento == item:
            return True
    return False
total = 0
cafes = ["espresso", "americano", "latte", "flat white", "cappuccino", "macchiato", "mocha"]
tamanios = ["mediano", "grande", "xl"]
servicios = ["1", "2"]

print("\nBienvenido! Elige qué quieres beber hoy: ")
print("\n--- MENÚ DE CAFÉS ---")
print("Espresso   $2.50      Cappuccino $3.00")
print("Americano  $3.00      Macchiato  $2.50")
print("Latte      $2.50      Mocha      $3.50")
print("Flat White $2.50")

valido = False
while not valido:   
    eleccion = input("\nTu elección: ").lower()
    for cafe, precio in [("espresso", 2.50), ("americano", 3.00), ("latte", 2.50),
                         ("flat white", 2.50), ("cappuccino", 3.00),
                         ("macchiato", 2.50), ("mocha", 3.50)]:
     valido = validar_opcion(eleccion, cafes)
    if not valido:   
     print("\nERROR: Ese café no está en el menú!")
    else:
     if eleccion == cafe:
      total += precio
      Coffe = True
    break

valido = False
while not valido:
    print("\n¿De qué tamaño quieres tu bebida?: ")
    print("Mediano: Sin costo extra")
    print("Grande:  $1.00")
    print("XL:      $1.50")
    eleccion_tamanio = input("\nElige: ").lower()
    valido = validar_opcion(eleccion_tamanio, tamanios)
    if not valido:
        print("ERROR: Ese tamaño no está en el menú!")
    else:
        if eleccion_tamanio == "grande":
            total += 1.00
        elif eleccion_tamanio == "xl":
            total += 1.50

valido = False
while not valido:
    print("\nAhora elige el servicio:")
    print("1. Para comer aquí: no extra")
    print("2. Para llevar:     $1.00")
    eleccion_service = input("Elige: ")
    valido = validar_opcion(eleccion_service, servicios)
    if not valido:
        print("ERROR: Ese servicio no existe!")
    else:
        if eleccion_service == "1":
            print("Elegiste: Para comer aquí")
            Service = True
        elif eleccion_service == "2":
            print("Elegiste: Para llevar")
            total += 1.00
            Service = True

print(f"\nTotal a pagar: ${total}")