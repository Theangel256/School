

class Perro():
    def __init__(
            self,
            num_patas: int,
            nombre: str, 
            edad: int, 
            genero: str, 
            color: hex, 
            raza: str, 
            vacunas: list,
            tiene_cola: bool,
            comidas_favoritas: str,
            estado_animo: str,
            coleteos: float,
            hambre: float
    ):
        self.num_patas = num_patas
        self.num_pasos = 0
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.color = color
        self.raza = raza
        self.vacunas = vacunas
        self.tiene_cola = tiene_cola
        self.comidas_favoritas = comidas_favoritas
        self.estado_animo = estado_animo
        self.coleteos = coleteos,
        self.hambre = hambre
        
    def ladrar(self, ladrido):
        return ladrido
    
    def correr(self, pasos_dados):
        self.num_pasos += pasos_dados
        print(f"He corrido {pasos_dados}m")
    def defecar(self, saciedad):
        self.hambre -=  saciedad
    def deluno(self, saciedad):
        self.hambre -= saciedad
    def cambiar_estado_animo(self, nuevo_estado):
        if self.estado_animo != nuevo_estado:
            print(f"El estado de ánimo cambió de '{self.estado_animo}' a '{nuevo_estado}'")
            self.estado_animo = nuevo_estado
    def comer(self, comida:str):
        print(f"Le has dado de comer a, {Firulais.nombre}")
        if(
            comida not in self.comidas_favoritas
            or not self.hambre
        ):
            self.cambiar_estado_animo("enojado")
            self.hambre -=60
            print("guau guau que asco")
        else:
            self.cambiar_estado_animo("feliz")
            self.coleteos = 100
            self.hambre += 40
            print("ñam ñam que rico")



Firulais = Perro(
     num_patas = 6,
     nombre = "Firulais", 
     edad = 35, 
     genero = "Macho", 
     color = "Cafe", 
     raza = "Chihuahua", 
     vacunas = ["covid", "rabia", "epatitis A"],
     tiene_cola = False,
     comidas_favoritas = ["basura", "pañales usados"],
     estado_animo = "meh",
     coleteos = 5,
     hambre = 100,
    )


print(Firulais)
print(Firulais.nombre)
print(Firulais.ladrar("Guau Guau!"))
Firulais.correr(10)
Firulais.correr(10*2)
Firulais.correr(10)
Firulais.correr(5)
print(Firulais.ladrar("Ya me canse we, digo woof woof"))
Firulais.correr(100)
print(Firulais.num_pasos)
Firulais.comer("basura")
print(Firulais.estado_animo)
print(Firulais.coleteos)
Firulais.comer("croquetas")
Firulais.defecar(40)
Firulais.hambre