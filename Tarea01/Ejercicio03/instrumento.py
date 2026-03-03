class Instrumento:
    def __init__(self, nombre, material, tipo):
        self.nombre = nombre
        self.__material = material
        self.__tipo = tipo
    def __str__(self):
        return (f"Instrumento: {self.nombre}\n"
                f"Material: {self.__material}\n"
                f"Tipo: {self.__tipo}")
    def getMaterial(self):
        return self.__material
    def getTipo(self):
        return self.__tipo
    def setMaterial(self, material):
        self.__material = material         
    def setTipo(self, tipo):
        self.__tipo = tipo
    
class Principal:
    ins1 = Instrumento("tarka", "madera", "viento")
    print(ins1)
    ins2 = Instrumento("tambor", "plastico, metal", "percusion")
    print(ins2)
