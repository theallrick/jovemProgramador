#Classe Retangulo: Crie uma classe que modele um retangulo:
#Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
#Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
#Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, 
#deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
from main import Retangulos

ret = Retangulos(2, 3)

ret.trocaLados(5, 5)
ret.retornaLados()
ret.perimetro()
ret.area()