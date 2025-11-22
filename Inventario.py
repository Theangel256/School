class Inventario():
    def __init__(self, nombre, capacidad_max, capacidad_actual):
        self.nombre = nombre
        self.__capacidad_max = capacidad_max
        self.__capacidad_actual = capacidad_actual

    @property
    def capacidad_max(self):
        return self.__capacidad_max
    @capacidad_max.setter
    def capacidad_max(self, valor):
        if valor >= self.__capacidad_actual and valor >= 10:
            self.__capacidad_max = valor
        else:
            print(
                (
                f"El valor {valor} no puede ser asignado como capacidad maxima "
                "porque es menor que 10 o por que es menor a la capacidad actual"
                )
            )
inv = Inventario(
    nombre="manzanas", 
    capacidad_actual=20, 
    capacidad_max=50
)

print(inv.capacidad_max)
inv.capacidad_max = 20
print(inv.capacidad_max)