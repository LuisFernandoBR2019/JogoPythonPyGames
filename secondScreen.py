import pygame

import firstScreen  # supondo que firstScreen está em outro arquivo

def secondScreen(tela, fonte):
    largura, altura = 800, 800

    # Cores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Carrega imagens dos monstros com transparência
    MONSTRO1 = pygame.image.load("assets/imagens/monstros/MONSTRO1.png").convert_alpha()
    MONSTRO2 = pygame.image.load("assets/imagens/monstros/MONSTRO2.png").convert_alpha()
    MONSTRO3 = pygame.image.load("assets/imagens/monstros/MONSTRO3.png").convert_alpha()
    MONSTRO4 = pygame.image.load("assets/imagens/monstros/MONSTRO4.png").convert_alpha()
    MONSTRO5 = pygame.image.load("assets/imagens/monstros/MONSTRO4.png").convert_alpha()

    # Carrega imagens de fundo
    terreno = pygame.image.load("assets/imagens/fundo.jpg").convert()
    terreno = pygame.transform.scale(terreno, (largura, altura))

    casa = pygame.image.load("assets/imagens/casa.png").convert_alpha()
    casa = pygame.transform.scale(casa, (largura, altura))

    # Carrega sprites do personagem
    player_images = {
        "frente": pygame.transform.scale(pygame.image.load("assets/imagens/personagem/personagem_frente.png").convert_alpha(), (50, 50)),
        "costas": pygame.transform.scale(pygame.image.load("assets/imagens/personagem/personagem_costas.png").convert_alpha(), (50, 50)),
        "esquerda": pygame.transform.scale(pygame.image.load("assets/imagens/personagem/personagem_esquerda.png").convert_alpha(), (50, 50)),
        "direita": pygame.transform.scale(pygame.image.load("assets/imagens/personagem/personagem_direita.png").convert_alpha(), (50, 50)),
    }

    player_x, player_y = 625, 220
    player_speed = 5
    player_direction = "frente"

    monsters = [
        {"rect": pygame.Rect(625, 520, 45, 45), "image": MONSTRO1, "msg": "Está bravo? Respire fundo 3 vezes!"},
        {"rect": pygame.Rect(500, 300, 50, 50), "image": MONSTRO2, "msg": "Triste? Que tal conversar com alguém?"},
        {"rect": pygame.Rect(200, 400, 50, 50), "image": MONSTRO3, "msg": "Está nervoso? Conte até 10 devagar."},
        {"rect": pygame.Rect(600, 150, 50, 50), "image": MONSTRO4, "msg": "Ansioso? Pense em algo que te acalma."},
        {"rect": pygame.Rect(755, 360, 50, 50), "image": MONSTRO5, "msg": "Ansioso? Pense em algo que te acalma."}
    ]

    current_msg = ""
    msg_timer = 0
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        moved = False
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
            player_direction = "esquerda"
            moved = True
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
            player_direction = "direita"
            moved = True
        if keys[pygame.K_UP]:
            player_y -= player_speed
            player_direction = "costas"
            moved = True
        if keys[pygame.K_DOWN]:
            player_y += player_speed
            player_direction = "frente"
            moved = True

        if moved:
            print(f"Posição do jogador: x={player_x}, y={player_y}")

        # Limita movimento dentro da tela
        player_x = max(0, min(player_x, largura - 50))
        player_y = max(0, min(player_y, altura - 50))


        player_rect = pygame.Rect(player_x, player_y, 50, 50)

        # Desenha fundo e elementos
        tela.blit(terreno, (0, 0))  # terreno (fundo)
        tela.blit(casa, (0, 0))     # casa (com transparência)
        tela.blit(player_images[player_direction], (player_x, player_y))  # personagem

        # Desenha monstros
        for m in monsters:
            tela.blit(m["image"], m["rect"].topleft)
            if player_rect.colliderect(m["rect"]):
                current_msg = m["msg"]
                msg_timer = pygame.time.get_ticks()
                # Se for o monstro 5, chama a outra tela
                if m["image"] == MONSTRO5:
                    firstScreen.firstScreen(tela, fonte)
                    print(m)
                    pygame.display.flip()
                    # depois que sair do firstScreen, pode voltar pro jogo ou encerrar

        # Exibe mensagem temporária
        if current_msg and pygame.time.get_ticks() - msg_timer < 4000:
            text_surface = fonte.render(current_msg, True, BLACK)
            tela.blit(text_surface, (largura // 2 - text_surface.get_width() // 2, 20))
        elif pygame.time.get_ticks() - msg_timer >= 4000:
            current_msg = ""

        pygame.display.flip()
        clock.tick(60)