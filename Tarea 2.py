class Mission():
    def __init__(self, nombre, dificultad):
        self.nombre = nombre
        self.__dificultad = dificultad
        self.__estado = "nueva"

    @property
    def dificultad(self):
        return self.__dificultad
    @dificultad.setter
    def dificultad(self, valor):
        if valor >= 1 and valor <= 10:
            self.__dificultad = valor
        else:
            return print(
                "El valor de la dificultad debe ser entre 1 y 10"
                )
        pass
    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, valor):
        if (
            (self.__estado == "nueva" and valor == "pendiente") or
            (self.__estado == "pendiente" and valor == "en progreso") or
            (self.__estado == "en progreso" and valor == "completada")
        ):
            self.__estado = valor
        else:
            print(
                f"El estado actual de la mision es {self.__estado} y la "
                f"misión no se puede completar aún"
                )
    @property
    def es_dificil(self):
        return True if self.__dificultad >= 7 else False
    def iniciar(self):
        if self.__estado != "completada":
            self.__estado = "en progreso"
        else:
            print(
                "Esta misión ya se completó"
                "Mejor a la próxima"
            )
    def completar(self):
        if self.__estado == "en progreso":
            self.__estado = "completada"
        else:
            print("La misión no se puede completar aún")
    def __str__(self):
        msg = f"""
    Misión      {self.nombre}
    Dificultad    {self.__dificultad}
    Estado      {self.__estado}
    Es Dificil? {self.es_dificil}
        """
        return msg

m = Mission("Tutorial", 1)
print(m)
m.estado = "completada"
m.estado = "pendiente"
print(m.estado)
m.completar()
print(m)