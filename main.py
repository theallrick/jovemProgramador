class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    def trocarCor(self, corNova):
        self.cor = corNova
    def mostrarCor(self):
        print(self.cor)
    def trocarMt(self, materialNovo):
        self.material = materialNovo
    def mostrarMt(self):
        print(self.material)

class Quadrado:
    def __init__(self, lado:float):
        self.lado = lado
    def mudarLado(self, novoLado):
        self.lado = novoLado
    def valorLado(self):
        print(self.lado)
    def calcArea(self):
        return(self.lado * self.lado)

class Retangulos:
    def __init__(self, ladoA:float, ladoB:float):
        self.ladoA = ladoA
        self.ladoB = ladoB
        print(ladoA)
        print(ladoB)
    def trocaLados(self, novoladoA, novoladoB):
        self.ladoA = novoladoA
        self.ladoB = novoladoB
    def retornaLados(self):
        return print((self.ladoA, self.ladoB))
    def perimetro(self):
        return print(2 * self.ladoA + 2 * self.ladoB)
    def area(self):
        return print(self.ladoA * self.ladoB)

class Contas:
    def __init__(self, numero, nome, saldo = 0):
        self.numero = numero
        self.correntista = nome
        self.saldo = saldo
    def alterarNome(self, nome):
        self.correntista = nome
    def deposito(self, valor):
        self.saldo = self.saldo + valor
    def saque(self, valor):
        self.saldo = self.saldo - valor
    def transferencia(self, outra, valor):
        self.saque(valor)

class People:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1
    def engordar(self, peso):
        self.peso += peso
    def emagrecer(self, peso):
        self.peso -= peso
    def crescer(self, altura):
        self.altura += altura
    def mostraPessoa(self):
        print(f'Nome: {self.nome}, idade: {self.idade} anos, peso: {self.peso}kg, altura: {self.altura}cm')

class Aluno:
    def __init__(self, nome, idade, ano, periodo):
        self.nome = nome
        self.idade = idade
        self.ano = ano
        self.periodo = periodo
    def trocarNome(self, nomeNovo):
        self.nome = nomeNovo
    def trocarIdade (self,idadeNova):
        self.idade = idadeNova
    def trocarAno (self,novoAno):
        self.ano = novoAno
    def trocarPeriodo(self, novoPeriod):
        self.periodo = novoPeriod
    def mostrarAluno (self):
        print(f'Nome: {self.nome}, idade: {self.idade}, serie: {self.ano}, turno: {self.periodo}')

class Nota(Aluno):
    def __init__(self, n1:float, n2:float, n3:float):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    def somaNotas(self, totalNotas):
        totalNotas = self.n1 + self.n2 + self.n3
        return totalNotas
    def mostrarNotas(self, totalNotas):
        print(totalNotas)
    def resultado(self, totalNotas):
        if totalNotas < 7:
            print(f'{self.nome} está reprovado')
        elif totalNotas == 10:
            print(f'{self.nome} está APROVADO COM DISTINÇÃO')
        else:
            print(f'{self.nome} está aprovado')
