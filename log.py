while True:
    print('----------Cadastro----------\n')
    usuario = input("Qual será seu usuario? ").capitalize()
    senhaCad = input("Qual será seu senha? ")
    qtdSenha= len(senhaCad)
    if qtdSenha<=6:
        print('Você precisa digitar pelo menos 6 caracteres!')
    else:
        print("Você está cadastrado no sistema. ")
        break
print('------------------Login-----------------\n')
while True:
    login = input("Qual seu login? ").capitalize()
    senha = input("Qual sua senha? ")
    if login != usuario and senha != senhaCad:
        print("Seu usuario ou senha está errado, digite novamente!")
    if login == usuario and senha == senhaCad:
        print("Seu login está correto.\n"), ('Sua senha está correta')
        print(f'{login} seja bem vindo, você está logado!')
        break
