
class Animal:
    def __init__(self, nombre, edad, nombreDueño):
        self._nombre = nombre
        self._edad = edad
        self._nombreDueño = nombreDueño
    def __str__(self):
        return f"nombre: {self._nombre}, edad: {self._edad}, nombre del Dueño: {self._nombreDueño}"

class Perro(Animal):
    def __init__(self, nombre, edad, nombreDueño, requiereBosal, ladraFuerte):
        super().__init__(nombre, edad, nombreDueño)
        self.__requiereBosal = requiereBosal
        self.__ladraFuerte = ladraFuerte
    def __str__(self):
        return super().__str__() + f" requiere bosal = {self.__requiereBosal}, ladra fuerte = {self.__ladraFuerte}"
    def __repr__(self):
        return self.__str__()
    def getEdad(self):
        return self._edad
class Gato(Animal):
    def __init__(self, nombre, edad, nombreDueño, cazaRatones, tomaLeche):
        super().__init__(nombre, edad, nombreDueño)
        self.__cazaRatones = cazaRatones
        self.__tomaLeche = tomaLeche
    def __str__(self):
        return super().__str__() + f" caza ratones = {self.__cazaRatones}, toma leche = {self.__tomaLeche}"
    def __repr__(self):
        return self.__str__()
class CentroVeterinario:
    def __init__(self, nombre, cantPerros, cantGatos):
        self.__nombre = nombre
        self.__cantPerros = cantPerros
        self.__cantGatos = cantGatos
        self.__perros = []
        self.__gatos = []
    def __str__(self):
        return f"nombre: {self.__nombre}, cantidadPerros: {self.__cantPerros}, lista de perros: {self.__perros}, cantidadGatos: {self.__cantGatos}, lista de gatos: {self.__gatos}"
    def addPerro(self, p):
        self.__perros.append(p)
        self.__cantPerros = self.__cantPerros + 1
    def addGato(self, g):
        self.__gatos.append(g)
        self.__cantGatos = self.__cantGatos + 1
    def ordenarPerros(self):
        self.__perros.sort(key=lambda p: (p.getEdad(), p._nombreDueño, p._nombre))
    def ordenarGatos(self):
        self.__gatos.sort(key=lambda g: (not g._Gato__tomaLeche, -g._edad, g._nombre))
    def verificarDueños(self):
        conteo = {}
        for p in self.__perros:
            dueño = p._nombreDueño
            conteo[dueño] = conteo.get(dueño, 0) + 1
        for g in self.__gatos:
            dueño = g._nombreDueño
            conteo[dueño] = conteo.get(dueño, 0) + 1
        for dueño, cantidad in conteo.items():
            if cantidad > 1:
                print(f"{dueño} tiene {cantidad} animales")
class Main:
    p1 = Perro("rocky", 6, "brandon", True, False)
    p2 = Perro("princesa", 4, "jose", False, True)
    p3 = Perro("perro 3", 6, "dueño 3", True, True)
    p4 = Perro("perro 4", 1, "dueño 4", False, False)
    g1 = Gato("michi", 2, "juan", False, True)
    g2 = Gato("trapecio", 5, "dueño 2", False, False)
    g3 = Gato("gato 3", 1, "dueño 3", True, False)
    g4 = Gato("gato 4", 3, "dueño 4", True, True)
    c1 = CentroVeterinario("centro 1", 0, 0)
    c1.addGato(g1)
    c1.addGato(g2)
    c1.addPerro(p1)
    c1.addPerro(p2)
    c2 = CentroVeterinario("centro 2", 0, 0)
    c2.addPerro(p3)
    c2.addPerro(p4)
    c2.addGato(g3)
    c2.addGato(g4)
    print(c1)
    c1.ordenarPerros()
    c1.ordenarPerros()
    print(c1)