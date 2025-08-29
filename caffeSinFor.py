# ¿Cuál versión crees que es más eficiente y por qué?
# La version con con for, es más pratico y se puede expander a mas problemas y mas facil de leer
# ¿Cuál o cuáles son las ventajas/desventajas de cada versión?
# con ifs, es mucho de leer y volver a leer y repetir y estar atento de las cadenas, 
# en especial en python con los indent exception
# con for, es muy facil de romperse y tedioso a la hora de programar ambientes que no estan para
# nada familiares con la forma de programar de otros
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
    cafe = ["cappuccino", "mocha", "macchiato","flat white","espresso","latte", "americano"]
    eleccion_de_cafe = input('Dame un cafe:').lower()
    if eleccion_de_cafe in cafe:
        print(f"Elegiste el cafe: {eleccion_de_cafe}")
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
    else: 
        print(f"El cafe {eleccion_de_cafe}, no existe.")
print("""
    Precio de los tamaños
    Mediano - Sin Costo Extra
    Largo   - + $20 MXN
    XL      - + $45 MXN""")
while not SizeValidity:
    size = ["mediano", "largo", "xl"]
    sizeSelection = input('Dame un tamaño:').lower()
    if sizeSelection in size:
        print(f"Elegiste el tamaño: {sizeSelection}")
        if(sizeSelection) == "largo":
            costo = costo + 20
        if(sizeSelection) == "xl":
            costo = costo + 45
        SizeValidity = True
    else:
        print(f"El Tamaño {sizeSelection}, no existe.")
print("""
    Precios:
    Aqui - Sin Costo Extra
    Para Llevar - + $30 MXN
    """)
while not DeliveryValidity:
    deliverySelection = input('Será para llevar? o comer aqui?:').lower()
    delivery = ["para llevar", "aqui"]
    if deliverySelection in delivery:
        print(f"Elegiste la opción: {deliverySelection}")
        if(deliverySelection) == "para llevar":
            costo = costo + 30
        DeliveryValidity = True
    else:
        print(f"La opción {deliverySelection}, no existe")
print(f"""
Elegiste el cafe {eleccion_de_cafe} {sizeSelection}
Lugar: {deliverySelection}

El total Sería ${costo} MXN
""")