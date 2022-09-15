from abc import ABC, abstractmethod
from cmath import pi


class Quadrado(ABC):
    def __init__(self,perimetro:float):
        self.perimetro = perimetro
    def areas(self,):
        print(f'esse valor {self.perimetro**2}')
class Triangulo(ABC):
    def __new__(self,base:float,altura:float):
        self.b = base
        self.a = altura
    def areasTriangulo(self):
        print(f'essa {self.b*self.a**2}')
class Circulo(ABC):
    def __init__(self,perimetro):
        self.perimetro = perimetro
    def areaMostrar(self):
        print(pi*self.perimetro**2)
class Pentagono(ABC):
    pass

a = Circulo(5)

a.areaMostrar()
