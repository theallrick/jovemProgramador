print("--------Cadastro--------")
nome = input("Qual seu será seu usuario?\n")
senha = str(input('Qual sua senha?\n'))
print('--------Login--------')
while True:
    nome_lg = input('Qual seu login?\n')
    senha_lg = str(input("Qual sua senha?\n"))

    if nome_lg.strip() or nome.strip() == '':
        print('Os campos devem ser preenchidos corretamente.')
    if nome_lg == nome and senha_lg == senha :
        print('Acesso Autorizado')
        break
    else:
        print('Acesso negado')x 