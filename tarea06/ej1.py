class Edificio:
    def __init__(self, nombre, superficie, cantDep):
        self.__nombre = nombre
        self.__superficie = superficie
        self.__cantDep = cantDep
        self.__deps = []
        self.__parqueo = None
    def addParqueo(self, p):
        self.__parqueo = p
    def addDepa(self, nroPuerta, nroHab, nroPiso):
        d = Departamento(nroPuerta, nroHab, nroPiso)
        self.__deps.append(d)
        self.__cantDep = self.__cantDep + 1
    def addHabitacion(self, nroPuertadelDep, nombre, tamanio, cantMuebles):
        for i in self.__deps:
            if nroPuertadelDep == i.getnroPuerta():
                i.agregarHab(nombre, tamanio, cantMuebles)
    def addMueble(self, nombredeHab, m):
        for i in self.__deps:
            for j in i.getHabs():
                if j.getNombre() == nombredeHab:
                    j.agregarMueble(m)
    def MasHabs(self, piso):
        c = 0
        aux = None
        for i in self.__deps:
            if i.getPiso() == piso:
                if i.getnroHabs() > c:
                    c = i.getnroHabs()
                    aux = i
        print(aux)
    def masMuebles(self):
        c = 0
        aux = None
        for i in self.__deps:
            for j in i.getHabs():
                if j.getcantMuebles() > c:
                    c = j.getcantMuebles()
                    aux = j
        print(aux)
    def __str__(self):
        return f"nombre: {self.__nombre}, superficie: {self.__superficie}, cantDep: {self.__cantDep}, PARQUEO {self.__parqueo}, DEPS {self.__deps}"
class Departamento:
    def __init__(self, nroPuerta, nroHab, nroPiso):
        self.__nroPuerta = nroPuerta
        self.__nroHab = nroHab
        self.__hab = []
        self.__nroPiso = nroPiso
    def agregarHab(self, nombre, tamanio, cantMuebles):
        h = Habitacion(nombre, tamanio, cantMuebles)
        self.__hab.append(h)
        self.__nroHab = self.__nroHab + 1
    def getnroPuerta(self):
        return self.__nroPuerta
    def getHabs(self):
        return self.__hab
    def getPiso(self):
        return self.__nroPiso
    def getnroHabs(self):
        return self.__nroHab
    def __str__(self):
        return f"nroPuerta: {self.__nroPuerta}, nroHab: {self.__nroHab}, nroPiso: {self.__nroPiso}, habs: {self.__hab}"
    def __repr__(self):
        return self.__str__()
class Habitacion:
    def __init__(self, nombre, tamanio, cantMuebles):
        self.__nombre = nombre
        self.__tamanio = tamanio
        self.__cantMuebles = cantMuebles
        self.__muebles = []
    def agregarMueble(self, m):
        self.__muebles.append(m)
        self.__cantMuebles = self.__cantMuebles + 1
    def getNombre(self):
        return self.__nombre
    def getcantMuebles(self): 
        return self.__cantMuebles
    def __str__(self):
        return f"nombre: {self.__nombre}, tamanio: {self.__tamanio}, cantmuebles: {self.__cantMuebles}, muebles: {self.__muebles}"
    def __repr__(self):
        return self.__str__()
class Mueble:
    def __init__(self, tipo, material):
        self.__tipo = tipo
        self.__material = material
    def __str__(self):
        return f"tipo {self.__tipo}, material {self.__material}"
    def __repr__(self):
        return self.__str__()
class Parqueo:
    def __init__(self, capacidad, cantAuto, precioH):
        self.__capacidad = capacidad
        self.__cantAuto = cantAuto
        self.__precioH = precioH
        self.__parqueo = []
    def agregarPlaca(self, p):
        if len(self.__parqueo) < self.__capacidad:
            self.__parqueo.append(p)
        self.__cantAuto = self.__cantAuto+1
    def __str__(self):
        return f"capacidad: {self.__capacidad}, cantAuto: {self.__cantAuto}, precioH: {self.__precioH}, parqueo: {self.__parqueo}"
        

class Main:
    m1 = Mueble("cama", "madera")
    m2 = Mueble("mesa", "plastico")
    m3 = Mueble("sofa", "madera")
    p1 = Parqueo(10, 0, 2)
    e1 = Edificio("edificio 1", 1000.5, 0)
    e1.addDepa(666, 0, 1)
    e1.addHabitacion(666, "hab1.666", 100, 0)
    e1.addHabitacion(666, "hab2.666", 200, 0)
    e1.addMueble("hab1.666", m1)
    e1.addMueble("hab1.666", m2)
    e1.addMueble("hab1.666", m3)

    e1.addDepa(777, 0, 1)
    e1.addHabitacion(777, "hab1.777", 119, 0)
    e1.addMueble("hab1.777", m1)


    e1.addParqueo(p1)
    p1.agregarPlaca("1H4J5")
    p1.agregarPlaca("AS8F97")
    p1.agregarPlaca("VBDA71")
    print(e1)

    e1.MasHabs(1)
    e1.masMuebles()