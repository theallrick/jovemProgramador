print('------------Cadastro-------------')

nome = (input("Qual seu será seu usuario?\n")).lower()
senha = str((input('Qual sua senha?\n')).lower())

print('-------------Login------------')
while True:
    nome_lg = (input('Qual seu login?\n')).lower()
    senha_lg = str((input("Qual sua senha?\n")).lower())

    if nome_lg == nome and senha_lg == senha :
        print('Seu usuario está correto')
        print("Sua senha está correta")
        print("Parabens, você está conectado")
        break
    elif nome_lg != nome :
        print("Seu usuario está incorreto")
    else:
        print("Falha na autentificação")