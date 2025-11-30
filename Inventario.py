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
    @property
    def capacidad_actual(self):
        return self.__capacidad_actual
    @capacidad_actual.setter
    def capacidad_actual(self, valor):
        if valor < 10:
            print(f"El valor {valor} es inválido! porque no puede ser menor a 10")
        elif valor > self.capacidad_max:
            print(f"El valor {valor} es inválido! por que es mayor a la capacidad maxima")
        else:
            self.__capacidad_actual = valor
    def porcentaje_de_ocupacion(self):
        return self.__capacidad_actual*100/self.capacidad_max
inv = Inventario(
    nombre="manzanas", 
    capacidad_actual=20, 
    capacidad_max=50
)

print(inv.capacidad_max)
inv.capacidad_max = 20
print(inv.capacidad_max)
inv.capacidad_actual = 12
print(inv.capacidad_actual)

print(f"El inventario esta al: {inv.porcentaje_de_ocupacion()}%")