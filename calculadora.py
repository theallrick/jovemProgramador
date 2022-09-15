print ('Aperte f para encerrar o programa\n')
while True:
    try:
        n1= int(input('Qual seu primeiro numero?\n'))
        n2= int(input('Qual o segundo numero?\n'))
        ope= input("Qual operação você escolhe?\n").lower()
    except:
        print('INVALIDO!', 'Digite corretamente!')
        continue
    

    if ope == 'soma' or ope == '+':
        print(f'A soma dos numeros é:\n {n1+n2}')
    if ope == 'subtração' or ope == '-':
        print(f'A subtração dos numeros é:\n {n1-n2}')
    if ope == 'multiplicação' or ope == '*':
        print(f'A multiplicação dos numeros é:\n {n1*n2}')
    elif ope == 'divisão' or ope == '/':
        print(f'A divisão dos numeros é:\n {n1/n2}')
    elif ope == 'f' or ope <= 'f':
        print("Operação encerrada!")
        break
    