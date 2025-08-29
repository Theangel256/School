Validity = False
costo = 0

def validarInput(valor_a_buscar: str, lista: list) -> bool:
    """
    Esta funcion busca el input del usuario en una lista de opciones

    Args:
        valor_a_buscar (Str): Opcion elegida por el usuario
        lista (list): Lista de opciones válidas

    Returns:
        (bool): Indica si el input existe dentro de las opciones
    """
    for i in lista:
        if valor_a_buscar == i:
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
while not Validity:
    eleccion_de_cafe = input('Dame un cafe:').lower()
    Validity = validarInput(eleccion_de_cafe, ["cappuccino", "mocha", "macchiato", "flat white", "latte", "americano"])
    if not Validity:
        Validity = False
    else:    
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
        Validity = True
print("""
    Precio de los tamaños
    Mediano - Sin Costo Extra
    Largo   - + $20 MXN
    XL      - + $45 MXN""")
Validity = False
while not Validity:
    sizeSelection = input('Dame un tamaño:').lower()
    Validity = validarInput(sizeSelection, ["mediano", "largo", "xl"])
    if not Validity:
        Validity = False
    else:    
        if(sizeSelection) == "largo":
            costo = costo + 20
        if(sizeSelection) == "xl":
            costo = costo + 45
        Validity = True
print("""
    Precios:
    Aqui - Sin Costo Extra
    Para Llevar - + $30 MXN
    """)
Validity = False
while not Validity:
    deliverySelection = input('Será para llevar? o comer aqui?:').lower()
    Validity = validarInput(deliverySelection, ["para llevar", "aqui"])
    if not Validity:
        Validity = False
    else:    
        if(deliverySelection) == "para llevar":
            costo = costo + 30
            Validity = True
print(f"""
El total Sería ${costo} MXN
""")