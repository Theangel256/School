class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def info(self):
        return f"Nombre: {self.nombre} | Vida: {self.vida}"

    def recibir_danio(self, d):
        self.vida -= d
        if self.vida < 0:
            self.vida = 0

    def atacar(self, enemigo, d):
        enemigo.recibir_danio(d)

class Guerrero(Personaje):
    def __init__(self, nombre, vida):
        super().__init__(nombre, vida)
        self.ataque = 15

    def info(self):
        base_info = super().info()
        return f"{base_info} | Clase: Guerrero"

    def atacar(self, enemigo, d=None):
        # El guerrero usa su propio ataque (15), ignorando d si se pasa, 
        # o podríamos usar d si quisiéramos flexibilidad, pero el requerimiento dice:
        # "haciendo que el parámetro d tome el valor del atributo propio ataque"
        d = self.ataque
        super().atacar(enemigo, d)
        print(f"El guerrero {self.nombre} ataca a {enemigo.nombre}")

def main():
    # Simulación de batalla
    print("--- Inicio de la Simulación ---")
    
    # Crear personajes
    p1 = Personaje("Aldeano", 50)
    g1 = Guerrero("Thorin", 100)
    
    # Mostrar info inicial
    print(p1.info())
    print(g1.info())
    print("-" * 20)

    # Batalla
    # Guerrero ataca a Personaje
    g1.atacar(p1, 0) # El segundo parametro es ignorado por la logica de Guerrero
    print(p1.info())
    print("-" * 20)

    # Personaje ataca a Guerrero
    print(f"{p1.nombre} contraataca!")
    p1.atacar(g1, 5)
    print(g1.info())
    print("-" * 20)

    # Guerrero ataca de nuevo
    g1.atacar(p1, 0)
    print(p1.info())
    print("-" * 20)

    # Guerrero ataca de nuevo (posible muerte)
    g1.atacar(p1, 0)
    print(p1.info())
    print("-" * 20)
    
    # Guerrero ataca de nuevo (remate)
    g1.atacar(p1, 0)
    print(p1.info())

if __name__ == "__main__":
    main()
