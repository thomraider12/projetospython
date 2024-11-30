print('Bem-vindo ao Quiz do Tomás!')
print('Responde a tudo com letras minusculas, e em extenso.')
answer=input('Estás preparado/a? (sim/não) : ')
score=0
total_questions=4
 
if answer.lower()=='não':
    print("Que pena não quereres jogar! Adeus :(")

if answer.lower()=='sim':
    answer=input('Questão 1: Quantos anos tem o Tomás? (por extenso) ')
    if answer.lower()=='onze':
        score += 1
        print('Correto!')
    else:
        print('Errado, a resposta certa era: "onze".')
 
 
    answer=input('Questão 2: Quanto é 5x5+5? ')
    if answer.lower()=='trinta':
        score += 1
        print('Correto!')
    else:
        print('Errado, a resposta certa era: "trinta". ')
 
    answer=input('Questão 3: Qual foi a língua de programação usada neste quiz? ')
    if answer.lower()=='python':
        score += 1
        print('Correto!')
    else:
        print('Errado, a resposta certa era: "python".')

    answer=input('Questão 4: Onde desagua o Rio Minho? ')
    if answer.lower()=='caminha':
        score += 1
        print('Correto!')
    else:
        print('Errado, a resposta certa era: "caminha".')
 
    print('Obrigado por jogares este pequeno Quiz, a tua pontuação é de',score,"perguntas certas!")
    mark=(score/total_questions)*100
    print('Conseguiste:',mark,"%")
    print('Adeus!')