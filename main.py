import random

def jogar():
    opcoes = ['pedra', 'papel', 'tesoura']
    
    while True:
        jogador = input("Escolha pedra, papel ou tesoura (ou sair para terminar o jogo): ").lower()
        if jogador == 'sair':
            print("Obrigado por jogar!")
            break
        if jogador not in opcoes:
            print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")
            continue
        
        computador = random.choice(opcoes)
        print("Computador escolheu:", computador)
        
        if jogador == computador:
            print("Empate!")
        elif (jogador == 'pedra' and computador == 'tesoura') or \
             (jogador == 'papel' and computador == 'pedra') or \
             (jogador == 'tesoura' and computador == 'papel'):
            print("Você venceu!")
        else:
            print("Você perdeu!")

if __name__ == "__main__":
    jogar()
