#Escreva a classe Veiculo contendo Peso em quilos (int), VelocMax em km/h (int) e
#Preco em R$ (float). Inclua um construtor que inicialize os dados com os valores recebidos como argumento.
#Acrescente uma função para a entrada de dados, getdata(), e uma função que imprima os dados.
class Veiculo:
    def __init__(self,peso:int, veloMax:int, preço:float):
        self.peso = peso
        self.veloMax = veloMax
        self.preço = preço
    
