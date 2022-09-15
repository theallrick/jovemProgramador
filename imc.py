peso = float(input("Qual seu peso?\n"))
altura = float(input('Qual sua altura?\n'))

imc = peso/(altura**2)
print(f'Seu IMC é igual a : {imc:.2f}')
