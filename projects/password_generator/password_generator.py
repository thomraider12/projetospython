import string
import random
 
 
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)
 
 
user_input = input("Quantos caractéres queres na password?")
 
 
while True:
 
    try:
 
        número_caracteres = int(user_input)
 
        if número_caracteres < 8:
 
            print("O nº de caracteres deve ser superior a 8.")
 
            user_input = input("Então agora, escreve um nº maior: ")
 
        else:
 
            break
 
    except:
 
        print("Coloca em nº.")
 
        user_input = input("Quantos caractéres queres na password?")
 
 
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
 
 
part1 = round(número_caracteres * (30/100))
part2 = round(número_caracteres * (20/100))
 
 
result = []
 
for x in range(part1):
 
    result.append(s1[x])
    result.append(s2[x])
 
for x in range(part2):
 
    result.append(s3[x])
    result.append(s4[x])
 
 
random.shuffle(result)
 

password = "".join(result)
print("Palavra-Passe forte:", password)