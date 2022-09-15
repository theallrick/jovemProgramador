#5.Considere o código abaixo e responda as questões:
# if (b1 == True):
#   c1 = True
# else:
#   if (b2 == True):
#       if (b3 == True):
#           c2 = True
#       else:
#           c3 = True
#       c4 = True
# c5 = True
# a.Se b1=V,b2=V e b3=F,quais comandos serão executados pelo algoritmo?
# b.Se b1 = F, b2 = V e b3 = F, quais comandos serão executados?
# c.Se b1 = F, b2 = V e b3 = V, quais comandos serão executados?
#d.Quais valores lógicos b1,b2 e b3 devem receber para que somente o comando C5 seja executado?
#a - c2 = true
#b - c1 = true
#c - c1 = true
#d - b1=V b2=V e b3=V
b1= 1
b2= 2
b3= 3
if (b1 == True):
 c1 = True
else:
    if (b2 == True):
        if (b3 == True):
            c2 = True
        else:
            c3 = True
        c4 = True
c5 = True