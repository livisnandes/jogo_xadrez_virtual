import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações do tabuleiro
largura, altura = 800, 800
tamanho_celula = largura // 8
cor_clara = (255, 206, 158)
cor_escura = (209, 139, 71)

# Cores das peças
cor_peca_clara = (255, 255, 255)
cor_peca_escura = (0, 0, 0)

# Inicializar a tela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo de Xadrez')

# Carregar imagens das peças
peao_branco = pygame.image.load('peao_branco.png')  # Substitua pelo caminho da sua imagem
peao_preto = pygame.image.load('peao_preto.png')  # Substitua pelo caminho da sua imagem

# Função para desenhar o tabuleiro
def desenhar_tabuleiro():
    for linha in range(8):
        for coluna in range(8):
            cor = cor_clara if (linha + coluna) % 2 == 0 else cor_escura
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

# Função para desenhar as peças no tabuleiro
def desenhar_pecas(tabuleiro):
    for linha in range(8):
        for coluna in range(8):
            peca = tabuleiro[linha][coluna]
            if peca == 'P':
                tela.blit(peao_branco, (coluna * tamanho_celula, linha * tamanho_celula))
            elif peca == 'p':
                tela.blit(peao_preto, (coluna * tamanho_celula, linha * tamanho_celula))

# Função principal do jogo
def jogo_xadrez():
    tabuleiro_inicial = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]

    clock = pygame.time.Clock()

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        desenhar_tabuleiro()
        desenhar_pecas(tabuleiro_inicial)

        pygame.display.flip()
        clock.tick(30)

# Iniciar o jogo
jogo_xadrez()
