#4.Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem:
# "São múltiplos" ou "Não são múltiplos"
a = float(input("Valor de 'A': "))

b = float(input("Valor de 'B': "))

if not (a%b):
    print("São Múltiplos")
else:
    print("Não são Múltiplos")