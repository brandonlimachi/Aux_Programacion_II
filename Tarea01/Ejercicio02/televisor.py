class Televisor:
    def __init__(self, marca="", resolucion=0, tipo=""):
        self.__marca = marca
        self.__resolucion = resolucion
        self.__tipo = tipo
    def __str__(self):
        return (f"Televisor:\n"
                f"Marca: {self.__marca}\n"
                f"Resolución: {self.__resolucion}\n"
                f"Tipo: {self.__tipo}")
class Principal:
    tv1 = Televisor("Samsung", 1080, "LED")
    print(tv1)
    tv2 = Televisor()
    print(tv2)
