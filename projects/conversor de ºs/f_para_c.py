def converter(s):
    f = float(s)
    c = (f - 32) * 5/9
    return c

fahrenheit = input("Escreve os graus em Fahrenheit: ")
print("Temperatura em Celsius:", converter(fahrenheit))