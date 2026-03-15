from multimethod import multimethod
class Aula:
    @multimethod
    def __init__(self, nombre: str, piso: int):
        self.__nombre = nombre
        self.__piso = piso
        self.__matriz = []
    @multimethod
    def __init__(self, nombre: str, piso: int, matriz: list):
        self.__nombre = nombre
        self.__piso = piso
        self.__matriz = matriz
    @multimethod
    def mostrar(self):
        print("nombre del aula:", self.__nombre)
        print("piso:", self.__piso)
        print("lista de estudiantes:")
        for fila in self.__matriz:
            print(fila)
    @multimethod
    def mostrar(self, x: str):
        for i in range(1, len(self.__matriz)):
           for j in range(1, len(self.__matriz[i])):
               if self.__matriz[i][j] >= 51:
                   print(self.__matriz[i][j-1], "Aprobado")
               else:
                   print(self.__matriz[i][j-1], "Reprobado")
                   
                   
class Main:
    mat = [["Nombre estudiante", "nota sobre 100"], ["Luis", 67], ["Aracely", 89]]
    a1 = Aula("A1", 2)
    a1.mostrar()
    a1.mostrar("")
    a2 = Aula("A2", 5, mat)
    a2.mostrar()
    a2.mostrar("")

