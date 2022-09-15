nome= input("Qual seu nome? \n").capitalize()
idade= int(input('Qual sua idade? \n'))
altura= float(input('Qual sua altura? \n'))
peso= float(input('E qual seu peso? \n'))
ano = 2022 
nasc= (ano - idade)
imc= peso/(altura**2)
print(f'Olá!! {nome}, nascido no ano de {nasc} com {idade} anos, sua altura é de {altura:.2f}cm e {peso}kg com seu imc de {imc:.2f}.')