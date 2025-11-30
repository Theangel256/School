from queue import Full


CoffeValidity = False
SizeValidity = False
DeliveryValidity = False
costo = 0

def args(valor_a_buscar, lista):
    for i in lista:
        if valor_a_buscar.lower() == i.lower():
            print(f"Elegiste la opción: {i}")
            return True
    print(f"La opción {valor_a_buscar}, no existe")
    return False
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
    args(valor_a_buscar = eleccion_de_cafe, lista = ["cappuccino", "mocha", "macchiato", "flat white", "latte", "americano"])
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
print("""
    Precio de los tamaños
    Mediano - Sin Costo Extra
    Largo   - + $20 MXN
    XL      - + $45 MXN""")
while not SizeValidity:
    sizeSelection = input('Dame un tamaño:').lower()
    args(valor_a_buscar= sizeSelection, lista = ["mediano", "largo", "xl"])
    if(sizeSelection) == "largo":
        costo = costo + 20
    if(sizeSelection) == "xl":
        costo = costo + 45
        
    SizeValidity = True
print("""
    Precios:
    Aqui - Sin Costo Extra
    Para Llevar - + $30 MXN
    """)
while not DeliveryValidity:
    deliverySelection = input('Será para llevar? o comer aqui?:').lower()
    args(valor_a_buscar = deliverySelection, lista = ["para llevar", "aqui"])
    if(deliverySelection) == "para llevar":
        costo = costo + 30
    DeliveryValidity = True
print(f"""
Elegiste el cafe {eleccion_de_cafe} {sizeSelection}
Lugar: {deliverySelection}

El total Sería ${costo} MXN
""")


