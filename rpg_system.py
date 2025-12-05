"""
Sistema de Juego de Rol (RPG) simple.

Este módulo define un sistema básico de clases para un juego de rol, incluyendo
una clase base "Personaje" y subclases "Guerrero", "Mago" y "Arquero".
Permite simular batallas entre diferentes tipos de personajes.
"""

import random

class Personaje:
    """
    Clase base que representa un personaje genérico en el juego.

    Atributos:
        nombre (str): El nombre del personaje.
        _vida (int): La cantidad de vida actual del personaje. Es un atributo protegido.
    """
    def __init__(self, nombre, vida):
        """
        Inicializa un nuevo personaje.

        Args:
            nombre (str): El nombre del personaje.
            vida (int): La cantidad inicial de vida del personaje.
        """
        self.nombre = nombre
        self._vida = vida

    def info(self):
        """
        Devuelve una cadena con la información básica del personaje.

        Returns:
            str: Una cadena con el formato "Nombre: {nombre} | Vida: {vida}".
        """
        return f"Nombre: {self.nombre} | Vida: {self._vida}"

    def recibir_danio(self, d):
        """
        Reduce la vida del personaje en una cantidad especificada.

        Si la vida cae por debajo de 0, se ajusta a 0.

        Args:
            d (int): La cantidad de daño a recibir.
        """
        self._vida -= d
        if self._vida < 0:
            self._vida = 0

    def atacar(self, enemigo, d):
        """
        Realiza un ataque a un enemigo, causándole daño.

        Args:
            enemigo (Personaje): El personaje enemigo al que se ataca.
            d (int): La cantidad de daño que se inflige.
        """
        enemigo.recibir_danio(d)

class Guerrero(Personaje):
    """
    Clase que representa a un Guerrero, subclase de Personaje.
    Se especializa en combate cuerpo a cuerpo con un ataque fijo alto.

    Atributos:
        ataque (int): El valor de ataque fijo del guerrero (15).
    """
    def __init__(self, nombre, vida):
        """
        Inicializa un nuevo Guerrero.

        Args:
            nombre (str): El nombre del guerrero.
            vida (int): La vida inicial del guerrero.
        """
        super().__init__(nombre, vida)
        self.ataque = 15

    def info(self):
        """
        Extiende la información base añadiendo la clase del personaje.

        Returns:
            str: Cadena con información del personaje y "| Clase: Guerrero".
        """
        base_info = super().info()
        return f"{base_info} | Clase: Guerrero"

    def atacar(self, enemigo, d=None):
        """
        Ataca a un enemigo usando el atributo de ataque propio del guerrero.

        Ignora el parámetro "d" si se proporciona, usando siempre "self.ataque".
        Imprime un mensaje describiendo el ataque.

        Args:
            enemigo (Personaje): El enemigo a atacar.
            d (int, optional): El daño a infligir. Si es None, usa "self.ataque".
        """
        if d is None:
            d = self.ataque
        super().atacar(enemigo, d)
        print(f"El guerrero {self.nombre} ataca a {enemigo.nombre} con {d} de daño")

class Mago(Personaje):
    """
    Clase que representa a un Mago, subclase de Personaje.
    Tiene un ataque moderado fijo.

    Atributos:
        ataque (int): El valor de ataque fijo del mago (10).
    """
    def __init__(self, nombre, vida):
        """
        Inicializa un nuevo Mago.

        Args:
            nombre (str): El nombre del mago.
            vida (int): La vida inicial del mago.
        """
        super().__init__(nombre, vida)
        self.ataque = 10

    def info(self):
        """
        Extiende la información base añadiendo la clase del personaje.

        Returns:
            str: Cadena con información del personaje y "| Clase: Mago".
        """
        base_info = super().info()
        return f"{base_info} | Clase: Mago"

    def atacar(self, enemigo, d=None):
        """
        Ataca a un enemigo usando el atributo de ataque propio del mago.

        Ignora el parámetro "d" si se proporciona, usando siempre "self.ataque".
        Imprime un mensaje describiendo el ataque.

        Args:
            enemigo (Personaje): El enemigo a atacar.
            d (int, optional): El daño a infligir. Si es None, usa "self.ataque".
        """
        if d is None:
            d = self.ataque
        super().atacar(enemigo, d)
        print(f"El mago {self.nombre} ataca a {enemigo.nombre} con {d} de daño")

class Arquero(Personaje):
    """
    Clase que representa a un Arquero, subclase de Personaje.
    Tiene un ataque variable y capacidad de esquivar daño.

    Atributos:
        ataque (int): Propiedad que devuelve un valor de ataque aleatorio entre 0 y 20.
    """
    def __init__(self, nombre, vida):
        """
        Inicializa un nuevo Arquero.

        Args:
            nombre (str): El nombre del arquero.
            vida (int): La vida inicial del arquero.
        """
        super().__init__(nombre, vida)

    @property
    def ataque(self):
        """
        Calcula el valor del ataque del arquero.

        Returns:
            int: Un número aleatorio entre 0 y 20.
        """
        return random.randint(0, 20)

    def info(self):
        """
        Extiende la información base añadiendo la clase del personaje.

        Returns:
            str: Cadena con información del personaje y "| Clase: Arquero".
        """
        base_info = super().info()
        return f"{base_info} | Clase: Arquero"

    def atacar(self, enemigo, d=None):
        """
        Ataca a un enemigo usando un valor de ataque aleatorio.

        Obtiene el daño de la propiedad "self.ataque".
        Imprime un mensaje describiendo el ataque.

        Args:
            enemigo (Personaje): El enemigo a atacar.
            d (int, optional): El daño a infligir. Si es None, usa "self.ataque".
        """
        if d is None:
            d = self.ataque
        super().atacar(enemigo, d)
        print(f"El arquero {self.nombre} ataca a {enemigo.nombre} con {d} de daño")

    def recibir_danio(self, d):
        """
        Recibe daño con posibilidad de reducción por agilidad.

        Calcula una reducción aleatoria entre 0 y 2.
        Si la reducción es mayor a 1, imprime un mensaje de "impacto reducido".
        Resta el daño final (daño original - reducción) a la vida.

        Args:
            d (int): La cantidad de daño entrante.
        """
        reduccion = random.randint(0, 10)
        if reduccion > 5:
            print(f" (impacto reducido en {reduccion} unidades por agilidad)")
        
        dano_final = d - reduccion
        if dano_final < 0:
            dano_final = 0
            
        self._vida -= dano_final
        if self._vida < 0:
            self._vida = 0

def main():
    """
    Función principal para ejecutar la simulación de batalla.

    Crea instancias de Personaje, Guerrero, Mago y Arquero.
    Simula una serie de ataques entre ellos y muestra el estado de cada uno.
    """
    # Simulación de batalla
    print("--- Inicio de la Simulación ---")
    
    # Crear personajes
    p1 = Personaje("Aldeano", 50)
    g1 = Guerrero("Thorin", 100)
    m1 = Mago("Gandalf", 80)
    a1 = Arquero("Legolas", 90)
    
    # Mostrar info inicial
    print(p1.info())
    print(g1.info())
    print(m1.info())
    print(a1.info())
    print("-" * 20)

    # Batalla
    # Guerrero ataca a Personaje
    g1.atacar(p1) 
    print(p1.info())
    print("-" * 20)

    # Personaje ataca a Guerrero
    print(f"{p1.nombre} contraataca!")
    p1.atacar(g1, 5)
    print(g1.info())
    print("-" * 20)

    # Guerrero ataca de nuevo
    g1.atacar(p1)
    print(p1.info())
    print("-" * 20)

    # Guerrero ataca de nuevo (posible muerte)
    g1.atacar(p1)
    print(p1.info())
    print("-" * 20)
    
    # Guerrero ataca de nuevo (remate)
    g1.atacar(p1)
    print(p1.info())
    print("-" * 20)

    # Mago entra en combate
    print("El Mago entra en acción!")
    m1.atacar(g1) 
    print(g1.info())
    print("-" * 20)
    
    # Guerrero ataca a Mago
    g1.atacar(m1)
    print(m1.info())
    print("-" * 20)

    # Mago ataca a Guerrero
    m1.atacar(g1)
    print(g1.info())
    print("-" * 20)

    # Arquero entra en combate
    print("El Arquero entra en acción!")
    a1.atacar(g1) 
    print(g1.info())
    print("-" * 20)

    # Arquero ataca a Guerrero
    a1.atacar(g1)
    print(g1.info())
    print("-" * 20)

    # Arquero ataca a Guerrero
    a1.atacar(g1)
    print(g1.info())
    print("-" * 20)
    
    # Guerrero ataca a Arquero
    g1.atacar(a1)
    print(a1.info())
    print("-" * 20)

    # GOLPE CRITICO DEL GUERRERO
    print("¡GOLPE CRITICO DEL GUERRERO!")
    g1.atacar(a1, 81) # Forzamos 81 de daño
    print(a1.info())
    print("-" * 20)

if __name__ == "__main__":
    main()
