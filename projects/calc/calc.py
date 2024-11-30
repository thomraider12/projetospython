def calculator():
    while True:
        calculacao = input("Escreve uma operação matemática, ou escreve 'e' para sair: ")
        
        if calculacao == 'e':
            print("Adeus!")
            break
        
        try:
            resultado = eval(calculacao)
            print("Resultado:", resultado)
        except (SyntaxError, NameError):
            print("Operação inválida. Tente novamente.")
        except (ZeroDivisionError):
            print("Não é possível dividir por zero.")

calculator()