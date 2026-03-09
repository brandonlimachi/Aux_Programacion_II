class Bus:
    def __init__(self, nroPasajeros: int, pasaje: float, asientos: int):
        self.nroPasajeros = nroPasajeros
        self.pasaje = pasaje
        self.asientos = asientos
    def sube(self, x):
        self.nroPasajeros = self.nroPasajeros + x
    def cobrar(self):
        return self.nroPasajeros * self.pasaje
    def asientosDispomibles(self):
        return self.asientos - self.nroPasajeros
    def __str__(self):
        return f"numero de pasajeros: {self.nroPasajeros}, total cobrado: {self.cobrar()} bs, asietos disponibles: {self.asientosDispomibles()}"

class Main:
    bus1 = Bus(10, 1.50, 20)
    print(bus1)
    bus1.sube(5)
    print(bus1)
