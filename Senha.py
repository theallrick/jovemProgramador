senha = str(input("Digite uma senha: \n"))

if len(senha) < 5:
    print('Sua senha é muito curta')
elif len (senha) > 12:
    print('Sua senha é muito longa')
else:
    print('Sua senha foi cadastrada com sucesso!')