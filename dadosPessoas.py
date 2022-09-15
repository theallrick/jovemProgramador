#2.Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual,calcule e mostre:
# a.a idade dessa pessoa em anos;
# b.a idade dessa pessoa em meses;
# c.a idade dessa pessoa em dias; (considere mês sempre com 30 dias)
# d.a idade dessa pessoa em semanas.(considere que há exatamente 4semanas em cada mês)
nome = input("Qual seu nome?\n").capitalize()
idade = int(input("Qual o ano que você nasceu? \n"))
anos = 2022 - idade
meses = anos * 12
dias = anos * 365
seman = anos * 48 
print(f'{nome} sua idade é \n',f"Anos: {anos}\n",f"Meses: {meses}\n",f'Dias: {dias}\n',f'Semanas: {seman}')
    