import pyautogui
import time

escolha = input("O que queres que ele te escreva automaticamente?\nR: ")

time.sleep(1)
print("Ok. 5 segundos e começa...\nDica: carrega em Ctrl+C no terminal para cancelar.")
time.sleep(5)

while True:
    pyautogui.write(escolha)
    pyautogui.press("enter")
    print(escolha)
    time.sleep(2)