import Adivinhacao
import forca

def escolhe_jogo():
    print('*********************************')
    print('Escolha qual jogo você quer jogar!')
    print('*********************************')

    print('(1) Adivinhação | (2) Jogo da Forca')

    jogo = int(input('Digite o número de qual jogo você quer jogar: \n'))
    if(jogo == 1):
        print('Jogando Adivinhação')
        Adivinhacao.jogar()
    elif(jogo == 2):
        print('Jogando Jogo da Forca')
        forca.jogar()

if(__name__ == "__main__")  :
    escolhe_jogo()