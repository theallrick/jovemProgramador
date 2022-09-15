def tabuada():
    while True:
        h = input('Você quer saber a tabuada?''(S-sim N-Não)\n').upper()
        if h == 'S':
            numero = int(input('Qual numero você quer saber a tabuada? \n'))
            for i in range(0,11):
                print(f'{i} x {numero} = {numero*i}')
        else:
            print('Serviço Finalizado!')
            break

class Data:
    def data(datas):
        anos = datas-2022
        meses = anos * 12
        dias = anos * 365
        seman = anos * 48


    


