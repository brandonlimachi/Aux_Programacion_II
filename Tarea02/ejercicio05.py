
class Minecraft:
    def __init__(self, player: str, nroDiamantes: int, listaPlayers=[], diamantes=[]):
        self.__player = player
        self.__nroDiamantes = nroDiamantes
        self.listaPlayers = listaPlayers
        self.diamantes = diamantes
    def stack(self):
        return self.__nroDiamantes // 64
    def addPlayers(self):
        self.listaPlayers.append(self.__player)
    def addNewPlayer(self, x):
        self.listaPlayers.append(x)
    def addDiamantes(self):
        self.diamantes.append(self.__nroDiamantes)
    def mayor(self):
        m = 0
        for i in self.diamantes:
            if i > m:
                m=i
        return m
    def totald(self): 
        suma = 0
        for i in self.diamantes:
            suma = suma + i
        return suma 
    def __str__(self):
        return f"player: {self.__player}, numero de diamantes: {self.__nroDiamantes}, numero de stack de diam: {self.stack()}"
    def lista(self):
        return f"lista de jugadores: {self.listaPlayers}, mayor numero de diamantes: {self.mayor()}, total de diamantes en el server: {self.totald()}"
class Main:
    player1 = Minecraft("playerr1", 64)
    player1.addPlayers()
    player1.addDiamantes()
    print(player1)
    player2 = Minecraft("player2", 40)
    player2.addPlayers()
    player2.addDiamantes()
    print(player2)
    player3 = Minecraft("player3", 130)
    player3.addPlayers()
    player3.addDiamantes()
    print(player3)
    player4 = Minecraft("player4", 3)
    player4.addPlayers()
    player4.addDiamantes()
    print(player4)
    player5 = Minecraft("player5", 230)
    player5.addPlayers()
    player5.addDiamantes()
    print(player5)
    player6 = Minecraft("player6", 10)
    player6.addPlayers()
    player6.addDiamantes()
    print(player6)
    player7 = Minecraft("player7", 65)
    player7.addPlayers()
    player7.addDiamantes()
    print(player7)
    player8 = Minecraft("player8", 67)
    player8.addPlayers()
    player8.addDiamantes()
    print(player8)
    player9 = Minecraft("player9", 1)
    player9.addPlayers()
    player9.addDiamantes()
    print(player9)
    player10 = Minecraft("player10", 345)
    player10.addPlayers()
    player10.addDiamantes()
    print(player10)

    lista1 = Minecraft("", 0)
    print(lista1.lista())
