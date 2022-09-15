class Personagem:
    def __init__(self, nome):
        self.__name = nome
        self.__health = 100
        self.__stamina = 50
        self.__life = 500
        self.__hungry = 50
    def mostrarPersonagem(self):
        print(f'Seu nome é {self.__name}, sua vida é de {self.__health}, você tem {self.__stamina} de energia e {self.__life} de mana e sua fome {self.__hungry}.')
    def correr(self):
        perdeFome = self.__hungry - 10
        perdeEnergia = self.__stamina - 10
        print(f'Você correu,por isso perdeu: fome e energia, agora precisa descansar.' )
        print(f'Esse é seu status atual: \nFome: {perdeFome} \nEnergia: {perdeEnergia}')   
        if self.__stamina <= 0:
            print(f'{self.__name} seu personagem desmaiou, pois você é um(a) maluco(a) que adora correr')
        else:
            print("Você precisa descansar doidio")
    def feitico(self, soltaPoder:int):
        soltaPoder = self.__life - soltaPoder
        perdeVida = self.__health - 50
        print(f'WOWWWW {self.__name}, você lançou um grandissimo poder, detonou uma capital inteira cara!!!!!!!!')
        print('Como seu poder teve efeito critico, triplicou o poder como também a perca de mana')
        print("Seu poder foi tão forte que acabou perdendo vida")
        print(f'Sua mana está em {soltaPoder}\nSua vida está {perdeVida}')
    def feitiçoFraco(self, poderFraco:int):
        poderFraco = self.__life - poderFraco
        print(f'WOWWWW {self.__name}, você lançou um grandissimo poder!!')
        print('O feitiço foi fraco, mas mesmo assim teve deveras efeito, infelizmente teve perda de mana')
        print(f'Sua mana agora é de {poderFraco}')
    def dormindo(self):
        print("Devido a toda a ação feita, você finalmente vai dormir")
        print("Dormir recupera todos os seu status, menos fome.")
        print(f"Você perde 20 de fome {self.__hungry - 20}")
    def comer(self):
        comendo = self.__hungry + 20
        print(f'Você come, então recupera sua fome {comendo}')
        
    