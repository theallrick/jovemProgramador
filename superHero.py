class Humano:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
class Inseto:
    def __init__(self,nome,venenoso:bool, alado:bool):
        self.nome = nome
        self.venenoso = venenoso
        self.alado = alado
class SuperHeroi(Humano, Inseto):
    def __init__(self, nome, idade, codNome, poder):
        self.nome = nome
        self.idade = idade
        self.codNome = codNome    
        self.poder = poder
    def show(self):
        print(f'{self.nome} você tem {self.idade} seu codnome é {self.codNome} e seu poder é {self.poder}.' )

pessoa = SuperHeroi('henrique',17,'theallrick','fogo')

pessoa.show()
