#Classe Pessoa: Crie uma classe que modele uma pessoa:

#Atributos: nome, idade, peso e altura
#Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
from main import People

lay = People('Henrique', 17, 84, 192)
lay.mostraPessoa()
lay.envelhecer()
lay.engordar(5)
lay.crescer(3)
lay.mostraPessoa()