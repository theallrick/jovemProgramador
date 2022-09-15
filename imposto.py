nome= input("Qual seu nome?")
salario= float(input("Qual o seu salario?"))
if (salario <= 1903.98):
    print ("Isento de desconto")
    print (nome, "seu salario é:")
elif (salario > 1903.98 and salario < 2826.65):
    print ("Imposto de 7,5% aplicado")
    print (nome, "seu salario é:")
    print (salario - (salario * 7.5 / 100))
elif (salario > 2826.65 and salario < 3751.06):
    print ("Imposto de 15% aplicado")
    print (nome, "seu salario é:")
    print (salario - (salario * 15.0 / 100))
elif (salario > 3751.06 and salario <4664.68):
    print ("Imposto de 22,5% aplicado")
    print (nome, "seu salario é:")
    print (salario - (salario * 22.5 / 100))
elif (salario > 4664.68 ):
    print ("Imposto de 27,5 aplicado")
    print (nome, "seu salario é:")
    print (salario - (salario * 27.5 / 100))
