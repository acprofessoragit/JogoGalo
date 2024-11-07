from random import randrange

# for i in range(10):
#     print(randrange(8))

tabuleiro = [ ['1','2','3'],['4','5','6'],['7','8','9']]
sinal_pc = 'X'
sinal_user = 'O'

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
    lista_livres = faz_lista_jogadas_livres(tabuleiro)
    while True:
        jogada = input('Qual a sua jogada? ')
        if jogada in lista_livres:
            break
        print('Posição',jogada,'ocupada, tente novamente!!!')
    linha, coluna = linha_coluna(jogada)
    tabuleiro[linha][coluna] = sinal_user
    return tabuleiro

def linha_coluna( jogada ):
    n = int(jogada)
    linha = (n - 1) // 3
    coluna = n - linha * 3 - 1
    return linha, coluna

def faz_lista_jogadas_livres(tabuleiro):
     # Esta função percorre o tabuleiro e constrói a lista de todos os quadrado livres;
    # a lista é constituída por tuplas, e cada tupla é o par de números de linha e coluna
    livres = []
    for linha in tabuleiro:
        for jogada in linha:
            if jogada != sinal_user and jogada != sinal_pc:
                livres.append(jogada)
    return livres



def vitoria_para(tabuleiro, sign):
    # Esta função analisa o estado do tabuleiro de modo a verificar se
    # o jogador usando '0's ou 'X's ganhou o jogo
    print("Em construção")


def faz_jogada(tabuleiro):
     # Esta função faz com que o computador faça uma jogada e atualiza o tabuleiro
    print("Em construção")

print('JOGO DO GALO\n\n')
resposta = input('Joga primeiro o computador (s/n)? ')
if resposta.strip().lower()[0] == 's':
    tabuleiro[1][1] = sinal_pc
    n_jogadas = 1
else:
    n_jogadas = 0
mostra_tabuleiro(tabuleiro)
tabuleiro = entrar_jogada(tabuleiro)
mostra_tabuleiro(tabuleiro)
