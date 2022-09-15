''''
frase = '            quero ser programador'

print(frase.upper())
#todas caixa alta
print(frase.lower())
#todas minusculas
print(frase.capitalize())
#primeira maior
print(frase.title())
#todas as primeiras
print(frase.strip())
#tirar espaço da frase
'''

'''
#login
print("Cadastro")
nome = input("Qual seu será seu usuario?\n ")
senha = int(input('Qual sua senha?\n '))
print('Login')
nome_lg = input('Qual seu login?\n ')
senha_lg = int(input("Qual sua senha?\n "))

if nome_lg.strip() or nome.strip() == '':
    print('Os campos devem ser preenchidos.')
if nome_lg == nome and senha_lg == senha :
    print('Acesso Autorizado')
else:
    print('Acesso negado')
'''

'''
#concatenação
w = 1
x = 2
y = 3
z = 4


print('minha idade é: ', x)
print('minha idade é: {} {} {} {}'.format(w,x,y,z))
print(f'Minha idade é: {w} {x} {y} {z}')

arredondar = round(x)
arredondar = round(x, 2)   # dps da , é o numero de casas
'''
'''
#if else elif
x = 50
y = 20

if x < y:
    print('x é menor y')

elif x == y:
    print("x é igual y")

elif x >= 50 and x <= 100:
    print('x está entre 50 e 100')

elif x > 10 and x < 15:
    print ('x esta entre 50 e 100')

else :
    print (' X é maior que Y')
'''
'''
#repetidor (Quebrar Crtl + C)
x = 0

while x == 100:
    print("Estou dentro da sala")
    x += 1

#intervalo/ quantidade de vezes
for i in range(0,11):
    print(f'vez (i)')
print('Estou fora do loop')
'''
'''
#cada palavra do x
x = 'python'
for i in range(0, len (x)):
    print(x[i])
'''

