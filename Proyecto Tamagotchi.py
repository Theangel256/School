class Tamagotchi():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad
        self.__hambre = 100
        self.__sed = 100
        self.__energia = 100
        self.__felicidad = 100
        self.__salud = 100
        self.__limpieza = 100
        self.__salud = 100
        self.__vivo = True

    def __str__(self):
        msg = f"""
        Estado General
    Nombre      {self.nombre}
    Edad        {self.__edad}
    Hambre      {self.__hambre}
    Sed         {self.__sed}
    Energia     {self.__energia}
    Felicidad   {self.__felicidad}
    Salud       {self.__salud}
    Esta vivo?  {self.__vivo}
        """
        return msg
    def comer(self):
        if self.__hambre > 100:
            return print(f"{self.nombre} ya comió demasiado!")
        self.__hambre += 40
    def beber(self):
        if self.__sed > 100:
            return print("Voy a explotar de agua papá")
        self.__sed += 20
    def jugar(self):
        print("Jijija")
        self.__felicidad += 20
    def dormir(self):
        self.__energia += 30
    
SonGoku = Tamagotchi("Kakaroto", 1)
print(SonGoku)