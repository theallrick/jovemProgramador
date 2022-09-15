#6.O código a seguir está certo?Se não estiver,como você iria resolver e qual é o problema.
# i = 0
# while i < 10:
#   print(i)
#   if i == 7:
#       break
#adicionando um numero a cada casa, com o i += 1, é possivel arrumar o algoritimo para que não fique num ciclo infinito
i = 0
while i < 10:
    i += 1
    print(i)
    if i == 7:
        break
    