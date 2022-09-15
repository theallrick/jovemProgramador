#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os 
#métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
from main import Contas
c1 = Contas(123, "Fagner")
c2 = Contas(456, "Xose")
c1.deposito(50)
c1.saque(10)
c1.deposito(100)
c1.transferencia(c2, 50)
c2.saque(30)
print ("Saldo c1: %i, Saldo c2: %i" % (c1.saldo, c2.saldo))
c1.alterarNome("Ferg")
print (c1.correntista)