from random import randrange

# for i in range(10):
#     print(randrange(8))

tabuleiro = [ ['1','2','3'],['4','5','6'],['7','8','9']]

def mostra_tabuleiro(tabuleiro):
    # Esta função aceita um parâmetro contendo o estado corrente do tabuleiro
    # e imprime o tabuleiro na consola
    for linha in tabuleiro:
        print('+ ', '-' *( 6 * 3 + 4), ' +')
        for jogada in linha:
            print('|',' '*2,jogada,' '*2, end='')
        print('|')
    print('+ ', '-' *( 6 * 3 + 4), ' +')


def entrar_jogada(tabuleiro):
    # Esta função aceita o o tabuleiro do jogo, pergunta ao utilizador acerca da jogada
    # verifica a jogada e atualiza o tabuleiro de acordo com a decisão do jogador
    print("Em construção")


def faz_lista_jogadas_livres(tabuleiro):
     # Esta função percorre o tabuleiro e constrói a lista de todos os quadrado livres;
    # a lista é constituída por tuplas, e cada tupla é o par de números de linha e coluna
     print("Em construção")


def vitoria_para(tabuleiro, sign):
    # Esta função analisa o estado do tabuleiro de modo a verificar se
    # o jogador usando '0's ou 'X's ganhou o jogo
    print("Em construção")


def faz_jogada(tabuleiro):
     # Esta função faz com que o computador faça uma jogada e atualiza o tabuleiro
    print("Em construção")


mostra_tabuleiro(tabuleiro)