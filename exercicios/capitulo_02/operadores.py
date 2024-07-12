lista = [10, 20, 30, 40, 50]

valor= int(input('digite o numero para ver se está na lista'))

if valor in lista:
    print(f"O valor {valor} está na lista.")
else:
    print(f"O valor {valor} não está na lista.")