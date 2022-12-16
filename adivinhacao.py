import random


nivel_facil = 1
nivel_medio = 2
nivel_dificil = 3
rodada = 1
numero_secreto = random.randrange(1,101)
pontos = 1000
total_de_tentativas = 0

print(" Bem vindo(a) ao Jogo de Adivinhação! ")
print("**************************************")

jogador = input("    Como posso te chamar? ")
print(" ")
print("Olá " + jogador + ", vamos começar a jogar ! ")
print(" ")

print("Escolha o nível de dificuldade do jogo:")
print("(1) - Fácil")
print("(2) - Médio")
print("(3) - Difícil")
print(" ")
nivel = int(input("Digite o Nível: "))
print(" ")

while(nivel>=0):
    if(nivel == nivel_facil):
        total_de_tentativas = 10
        print(" ")
        print("Nível escolhido - Fácil")
        break
    elif(nivel == nivel_medio):
        total_de_tentativas = 7
        print(" ")
        print("Nível escolhido - Médio")
        break
    elif(nivel == nivel_dificil):
        total_de_tentativas = 3
        print(" ")
        print("Nível escolhido - Difícil")
        break
    else:
        print("Ops, não identificamos o nível, digite novamente por favor!")
        print("Você deve escolher um número entre 1 e 3")
        print(" ")
        nivel = int(input("Digite o Nível: "))


print("**************************************")
print("            Vamos Jogar! ")
print("**************************************")
print(" ")


for rodada in range(1, total_de_tentativas + 1):
    print("Total de tentativas: {}/{}".format(rodada, total_de_tentativas))

    chute_jogador = input("Digite o número: ")
    print(" ")
    print("Você escolheu o número ", chute_jogador)
    chute_int = int(chute_jogador)

    if(chute_int < 1 or chute_int > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    venceu = numero_secreto == chute_int
    maior = chute_int > numero_secreto
    menor = chute_int < numero_secreto

    if(venceu):
        print(" ")
        print("Acertou, parabéns!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")

    pontos_perdidos = abs(numero_secreto - chute_int)
    pontos = pontos - pontos_perdidos
print("Pontos: ",pontos,"pts")
print("Fim do jogo!")