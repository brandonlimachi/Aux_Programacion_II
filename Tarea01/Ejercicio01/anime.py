class Anime:
    def __init__(self, nombre, genero, nroEpisodios, episodios):
        self.nombre = nombre              
        self.genero = genero              
        self.__nroEpisodios = nroEpisodios 
        self.__episodios = []            
class Main:
    a1 = Anime("Naruto", "Shonen", 220,"")
    a2 = Anime("Jujustu kaisen", "Shonen", 76,"") 
    print(a1)