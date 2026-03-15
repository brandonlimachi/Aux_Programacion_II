from multimethod import multimethod
class Videojuego:
    @multimethod
    def __init__(self):
        self.__nombre = "vacio"
        self.__plataforma = "vacio"
        self.__cantJugadores = 0
    @multimethod
    def __init__(self, nombre: str, plataforma: str):
        self.__nombre = nombre
        self.__plataforma = plataforma
        self.__cantJugadores = 0
    @multimethod
    def __init__(self, nombre: str, plataforma: str, cantJugadores: int):
        self.__nombre = nombre
        self.__plataforma = plataforma
        self.__cantJugadores = cantJugadores
    @multimethod
    def addJugadores(self):
        self.__cantJugadores = self.__cantJugadores + 1
    @multimethod
    def addJugadores(self, x: int):
        self.__cantJugadores = self.__cantJugadores + x
    def __str__(self):
        return f"nombre: {self.__nombre}, plataforma: {self.__plataforma}, cantidad de jugadores: {self.__cantJugadores}"

class Main:
    v1 = Videojuego()
    print(v1)
    v2 = Videojuego("minecraft", "xbox")
    v2.addJugadores()
    v2.addJugadores(100)
    print(v2)
    v3 = Videojuego("lefsito", "pc", 100000)
    print(v3)
