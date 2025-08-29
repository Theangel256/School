Validity = False
total = 0
deliveryArray = {
    "para llevar": { "price": 30 },
    "aqui": { "price": 0 }
    }
sizes = {
    "mediano": { "price": 0 }, 
    "largo": { "price": 25 },
    "xl": { "price": 45 }
    }
coffes = { "cappuccino": { "price": 53, },
    "mocha": { "price": 78 },
    "macchiato": { "price": 69 },
    "flat white": { "price": 65 },
    "espresso": { "price": 58 },
    "latte": { "price": 41 },
    "americano": { "price": 49 }
    }

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
    eleccion_de_cafe = input('\nDame un cafe:').lower()
    Validity = validarInput(eleccion_de_cafe, coffes)
    if Validity:
        total = coffes[eleccion_de_cafe]["price"]
print("""
    Precio de los tamaños
    Mediano - Sin Costo Extra
    Largo   - + $20 MXN
    XL      - + $45 MXN""")
Validity = False
while not Validity:
    sizeSelection = input('\nDame un tamaño:').lower()
    Validity = validarInput(sizeSelection, sizes)
    if Validity:
        total = total + sizes[sizeSelection]["price"]
print("""
    Precios:
    Aqui - Sin Costo Extra
    Para Llevar - + $30 MXN
    """)
Validity = False
while not Validity:
    deliverySelection = input('\nSerá para llevar? o comer aqui?:').lower()
    Validity = validarInput(deliverySelection, deliveryArray)
    if Validity:
        total = total + deliveryArray[deliverySelection]["price"]
print(f"""
El total Sería ${total} MXN
""")