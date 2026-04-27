class Libro:
    def __init__(self, nombre, autor, año):
        self.__nombre = nombre
        self.__autor = autor
        self.__año = año
    def __str__(self):
        return f"nombre: {self.__nombre}, autor: {self.__autor}, año: {self.__año}"
    def __repr__(self):
        return self.__str__()
    def getNombre(self):
        return self.__nombre
class Biblioteca:
    def __init__(self, nombre, cantLibros):
        self.__nombre = nombre
        self.__cantLibros = cantLibros
        self.__libros = []
    def addLibro(self, l):
        self.__libros.append(l)
        self.__cantLibros = self.__cantLibros + 1
    def __str__(self):
        return f"nombre: {self.__nombre}, cantidad de libros: {self.__cantLibros}, libros: {self.__libros}"
    def verificar(self, X):
        for l in self.__libros:
            if X == l.getNombre():
                print(l)
    def masLibros(self, other):
        if self.__cantLibros > other.__cantLibros:
            print(self)
        elif (self.__cantLibros < other.__cantLibros):
            print(other)
        else:
            print(self)
            print(other)
class Main:
    l1 = Libro("principito", "jose", 1997)
    l2 = Libro("ellosnotenianzapatos", "eduardo", 1994)
    l3 = Libro("sangredecampeon", "elias", 2003)
    l4 = Libro("diamantito", "mikecrack", 2015)
    b1 = Biblioteca("biblioteca 1", 0)
    b1.addLibro(l1)

    b2 = Biblioteca("biblioteca 2", 0)
    b2.addLibro(l3)
    b2.addLibro(l4)
    print(b1)
    print(b2)
    b1.verificar("principito")
    b1.masLibros(b2)