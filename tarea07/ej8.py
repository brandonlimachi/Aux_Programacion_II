class SueldoInvalidoException(Exception):
    pass
class CargoInvalidoException(Exception):
    pass

class Empleado:
    def __init__(self, nombre, cargo, sueldo):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__sueldo = sueldo
    def __repr__(self):
        return f"nombre: {self.__nombre}, cargo: {self.__cargo}, sueldo: {self.__sueldo}"
class Empresa:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__empleados = []
    def addEmpleado(self, cantidad):
        for j in range(cantidad):
            nombre = input("nombre: ")
            while True:
                try:
                    cargo = input("cargo: ")
                    for i in cargo:
                        if i.isdigit():
                            raise CargoInvalidoException("el atributo cargo no puede contener numeros")
                    break
                except CargoInvalidoException as e:
                    print(f"Error {e}. Ingrese correctamente el cargo")

            try:
                sueldo = float(input("sueldo: "))
                if sueldo < 2500: 
                    raise SueldoInvalidoException("el sueldo no puede ser menor al Salario Mínimo Nacional (2.500 Bs)")
            except SueldoInvalidoException as e:
                print(f"Error {e}. Se ha asignado automaticamente el sueldo minimo al empleado")
                sueldo = 2500
            e = Empleado(nombre, cargo, sueldo)
            self.__empleados.append(e)
    def __str__(self):
        return f"empresa: {self.__nombre}, lista de empleados = {self.__empleados}"
empresa = Empresa("Pil")
empresa.addEmpleado(4)
print(empresa)