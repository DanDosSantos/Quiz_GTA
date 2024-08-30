print("Seja muito bem vindo ao quis do Dan!")
opcao = input('Quer começar? (S/N) ')

if opcao != 'S':
    quit()

score = 0

print('Começando...')
print('Quem desenvolveu o jogo Grand Theft Auto {GTA}? \n (A) Rockstar Games \n (B) Ubisoft \n (C) Activision \n (D) EA \n')
resposta_1 = input('Resposta: ')

if resposta_1 == "A":
    print('Correto!')
    score += 1
else:
    print('Incorreto!')


print('Qual o nome do protagonista do jogo GTA Sana Andreas? \n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Carlos Jonhson \n')
resposta_2 = input('Resposta: ')

if resposta_2 == "B":
    print('Correto!')
    score += 1
else:
    print('Incorreto!')

print(f'Quiz acabou... Pontuação: {score}/2')