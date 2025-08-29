CoffeValidity = False
SizeValidity = False
DeliveryValidity = False
costo = 0
print("""      Bienvenido a la Coffe Shop!
      Tenemos variedad de productos de café!
      
      Precio de los cafés
      Cappuccino     - + $53 MXN
      Mocha          - + $78 MXN
      Macchiato      - + $69 MXN
      Flat White     - + $65 MXN
      Espresso       - + $58 MXN
      Latte          - + $41 MXN
      Americano      - + $49 MXN""")
while not CoffeValidity:
    eleccion_de_cafe = input('Dame un cafe:').lower()
    for cafe in ["Cappuccino", "Mocha", "Macchiato","Flat White","Espresso","Latte", "Americano"]:
        if eleccion_de_cafe == cafe.lower():
            print(f"Elegiste el cafe: {cafe}")
            if(eleccion_de_cafe) == "cappuccino":
                costo = costo + 53
            if(eleccion_de_cafe) == "mocha":
                costo = costo + 78
            if(eleccion_de_cafe) == "macchiato":
                costo = costo + 69
            if(eleccion_de_cafe) == "flat thite":
                costo = costo + 65
            if(eleccion_de_cafe) == "espresso":
                costo = costo + 58
            if(eleccion_de_cafe) == "latte":
                costo = costo + 41
            if(eleccion_de_cafe) == "americano":
                costo = costo + 49
            CoffeValidity = True
            break
    if CoffeValidity == False:
        print(f"El cafe {eleccion_de_cafe}, no existe.")

print("""
    Precio de los tamaños
    Mediano - Sin Costo Extra
    Largo   - + $20 MXN
    XL      - + $45 MXN""")
while not SizeValidity:
    sizeSelection = input('Dame un tamaño:').lower()
    for size in ["Mediano", "Largo", "XL"]:
        if sizeSelection == size.lower():
            print(f"Elegiste el tamaño: {size}")
            if(sizeSelection) == "largo":
                costo = costo + 20
            if(sizeSelection) == "xl":
                costo = costo + 45
            SizeValidity = True
            break
    if SizeValidity == False:
        print(f"El Tamaño {sizeSelection}, no existe.")
print("""
    Precios:
    Aqui - Sin Costo Extra
    Para Llevar - + $30 MXN
    """)
while not DeliveryValidity:
    deliverySelection = input('Será para llevar? o comer aqui?:').lower()
    for delivery in ["Para Llevar", "Aqui"]:
        if deliverySelection == delivery.lower():
            print(f"Elegiste la opción: {delivery}")
            if(deliverySelection) == "para llevar":
                costo = costo + 30
            DeliveryValidity = True
            break
    if DeliveryValidity == False:
        print(f"La opción {deliverySelection}, no existe")
print(f"""
Elegiste el cafe {cafe} {size}
Lugar: {delivery}

El total Sería ${costo} MXN
""")