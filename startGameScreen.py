import pygame  # Importa a biblioteca Pygame para criação do jogo
import sys     # Importa o módulo sys para poder encerrar o programa
from firstScreen import firstScreen  # Importa a função da primeira fase do jogo
from secondScreen import secondScreen  # Importa a função da primeira fase do jogo

# Inicializa todos os módulos do Pygame
pygame.init()

# Define as dimensões da janela do jogo
largura, altura = 800, 800

# Cria a janela do jogo com as dimensões definidas
tela = pygame.display.set_mode((largura, altura))

# Define o título da janela do jogo
pygame.display.set_caption("Monstros das Emoções")

# Cria uma fonte com o nome "arial" e tamanho 40 para exibir textos na tela
fonte = pygame.font.SysFont("arial", 40)

# Carregando imagem
telainicial_img = pygame.image.load("assets/imagens/inicial.jpeg")

# Define as cores que serão usadas (em formato RGB)
BRANCO = (255, 255, 255)

# Função que exibe a tela inicial do jogo
def tela_inicio():
    tela.blit(telainicial_img, (0, 0))  # Desenha a imagem no topo da tela

# Loop principal do jogo
while True:
    for evento in pygame.event.get():  # Captura todos os eventos (teclado, mouse, etc.)
        if evento.type == pygame.QUIT:  # Se o jogador clicar para fechar a janela
            pygame.quit()  # Encerra o Pygame
            sys.exit()     # Encerra o programa
        elif evento.type == pygame.KEYDOWN:  # Se alguma tecla for pressionada
            if evento.key == pygame.K_RETURN:  # Se a tecla pressionada for ENTER
                secondScreen(tela, fonte)  # Chama a função que inicia a primeira fase do jogo

    tela_inicio()  # Exibe a tela inicial a cada frame
    pygame.display.flip()  # Atualiza o conteúdo da janela com o que foi desenhado