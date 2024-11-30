def converter(s):
    c = float(s)
    f = (c * 9/5) + 32
    return f

celsius = input("Escreve os graus em Celsius: ")
print("Temperatura em Fahrenheit:", converter(celsius))
