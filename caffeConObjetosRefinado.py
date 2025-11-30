Validity = False
total = 0
deliveries = {
    "para llevar": { "price": 30 },
    "aqui": { "price": 0 }
    }
sizes = {
    "mediano": { "price": 0 }, 
    "largo": { "price": 25 },
    "xl": { "price": 45 }
    }
coffes = { 
    "cappuccino": { "price": 53, }, "mocha": { "price": 78 }, "macchiato": { "price": 69 },
    "flat white": { "price": 65 }, "espresso": { "price": 58 }, "latte": { "price": 41 }, "americano": { "price": 49 }
}
def search(valor_a_buscar: str, lista: dict) -> object:
    """
    Esta funcion busca el input del usuario en una lista de opciones

    Args:
        valor_a_buscar (Str): Opcion elegida por el usuario
        lista (list): Lista de opciones válidas

    Returns:
        (bool): Indica si el input existe dentro de las opciones
    """
    if valor_a_buscar in lista:
            print(f"Elegiste la opción: {valor_a_buscar}")
            return lista[valor_a_buscar]
    else:
            print(f"La opción {valor_a_buscar}, no existe")
            return None
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
    Validity = search(eleccion_de_cafe, coffes)
    if Validity != None:
        total = Validity["price"]
print("""
    Precio de los tamaños
    Mediano - Sin Costo Extra
    Largo   - + $20 MXN
    XL      - + $45 MXN""")
Validity = False
while not Validity:
    sizeSelection = input('\nDame un tamaño:').lower()
    Validity = search(sizeSelection, sizes)
    if Validity != None:
        total = total + Validity["price"]
print("""
    Precios:
    Aqui - Sin Costo Extra
    Para Llevar - + $30 MXN
    """)
Validity = False
while not Validity:
    deliverySelection = input('\nSerá para llevar? o comer aqui?:').lower()
    Validity = search(deliverySelection, deliveries)
    if Validity != None:
        total = total + Validity["price"]
print(f"""
El total Sería ${total} MXN
""")