

class animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
class mamífero(animal):
    def funcion_mamiferos(self):
        print("Los mamíferos son animales que dan a luz a sus crías.")
    
    def gato(self):  
        print("El gato es un mamífero.")
    
    def ornitorrinco(self):
        print("El ornitorrinco es un mamífero.")

class oviparo(animal):
    def funcion_oviparos(self):
        print("Los ovíparos son animales que ponen huevos.")
    
    def ornitorrinco(self):
        print("El ornitorrinco es un ovíparo.")
