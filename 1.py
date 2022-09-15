#Classe Bola: Crie uma classe que modele uma bola:
#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

from main import Bola

bola1 = Bola("Branca", 100, "Ferro")
bola2 = Bola('Amarelo', 20, 'Madeira')

bola1.mostrarCor()
bola2.mostrarCor()
bola2.trocarCor("Lilas")
bola2.mostrarCor()
bola1.mostrarMt()
bola2.mostrarMt()
bola1.trocarMt('Borracha')
bola1.mostrarMt()
