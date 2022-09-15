primeiro= int(input("Primeiro numero: "))
segundo = int(input("Segundo numero: "))
terceiro = int(input('Terceiro numero:'))

maior = primeiro
if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro
print ("O numero maior é:", maior)
menor = primeiro
if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro
print ('O menor numero é: ', menor)