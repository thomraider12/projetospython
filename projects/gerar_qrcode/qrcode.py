import pyqrcode 
from pyqrcode import QRCode 


print("Bom dia!\nEntraste num gerador do códigos QR!")
print("Queres texto (escreve 'text'), ou um url (escreve 'url')?")
text_url = input()

if text_url == 'text':
    print("\nEscreve o que queres no código QR: ")
    text = input()
    qr = pyqrcode.create(text)  
    qr.svg("qrcode.svg", scale = 8)
elif text_url == 'url':
    print("\nEscreve o URL que queres converter em código QR: ")
    url = input()
    qr = pyqrcode.create(url)
    qr.svg("qrcode.svg", scale = 8)
else:
    print("Opção inválida! Por favor, escolhe 'text' ou 'url'.")