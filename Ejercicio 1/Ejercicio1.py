

class libro:
    
    def __init__(self, titulo, año, autor, paginas):
        self.titulo = titulo
        self.año = año
        self.autor = autor
        self.paginas = paginas

    def printear(self):
        print(f"Título del libro: {self.titulo}\n")
        print(f"Año de publicación: {self.año}\n")
        print(f"Autor: {self.autor}\n")
        print(f"Páginas: {self.paginas}\n")

