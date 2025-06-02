import pygame
import sys
from firstScreen import firstScreen  # importa a primeira fase

pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Monstros das Emoções")
fonte = pygame.font.SysFont("arial", 40)

BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

def tela_inicio():
    tela.fill(PRETO)
    texto = fonte.render("Pressione ENTER para iniciar o jogo", True, BRANCO)
    rect = texto.get_rect(center=(largura // 2, altura // 2))
    tela.blit(texto, rect)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                firstScreen(tela, fonte)  # chama a função da fase

    tela_inicio()
    pygame.display.flip()