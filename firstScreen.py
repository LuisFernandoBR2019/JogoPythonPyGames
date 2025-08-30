import pygame

def firstScreen(tela, fonte):
    largura, altura = 800, 800

    # Cores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (200, 50, 50)
    GREEN = (0, 150, 0)
    BLUE = (70, 70, 200)

    # Carrega imagens dos monstros
    MONSTRO1 = pygame.image.load("assets/imagens/monstros/MONSTRO1.png").convert_alpha()
    MONSTRO2 = pygame.image.load("assets/imagens/monstros/MONSTRO2.png").convert_alpha()
    MONSTRO3 = pygame.image.load("assets/imagens/monstros/MONSTRO3.png").convert_alpha()
    MONSTRO4 = pygame.image.load("assets/imagens/monstros/MONSTRO4.png").convert_alpha()

    # Fundo
    terreno = pygame.image.load("assets/imagens/fundo.jpg").convert()
    terreno = pygame.transform.scale(terreno, (largura, altura))
    casa = pygame.image.load("assets/imagens/casa.png").convert_alpha()
    casa = pygame.transform.scale(casa, (largura, altura))

    # Player
    player_images = {
        "frente": pygame.transform.scale(pygame.image.load("assets/imagens/personagem/personagem_frente.png").convert_alpha(), (50, 50)),
        "costas": pygame.transform.scale(pygame.image.load("assets/imagens/personagem/personagem_costas.png").convert_alpha(), (50, 50)),
        "esquerda": pygame.transform.scale(pygame.image.load("assets/imagens/personagem/personagem_esquerda.png").convert_alpha(), (50, 50)),
        "direita": pygame.transform.scale(pygame.image.load("assets/imagens/personagem/personagem_direita.png").convert_alpha(), (50, 50)),
    }

    def criar_monstros():
        return [
            {
                "rect": pygame.Rect(625, 520, 45, 45), #Posições dos montros
                "image": MONSTRO1,
                "pergunta": "Qual a capital da França?",
                "opcoes": ["Londres", "Paris", "Roma", "Berlim"],
                "resposta_certa": "Paris",
                "answered": False
            },
            {
                "rect": pygame.Rect(500, 300, 50, 50),
                "image": MONSTRO2,
                "pergunta": "Quanto é 7 x 6?",
                "opcoes": ["42", "36", "40", "48"],
                "resposta_certa": "42",
                "answered": False
            },
            {
                "rect": pygame.Rect(200, 400, 50, 50),
                "image": MONSTRO3,
                "pergunta": "Qual o maior planeta do sistema solar?",
                "opcoes": ["Terra", "Marte", "Júpiter", "Saturno"],
                "resposta_certa": "Júpiter",
                "answered": False #Já foi respondida
            },
            {
                "rect": pygame.Rect(600, 150, 50, 50),
                "image": MONSTRO4,
                "pergunta": "Qual o resultado de 9 + 10?",
                "opcoes": ["19", "21", "18", "20"],
                "resposta_certa": "19",
                "answered": False
            }
        ]

    # Estado inicial
    monsters = criar_monstros()
    player_x, player_y = 625, 220
    player_speed = 5
    player_direction = "frente"
    current_monster = None
    show_question = False
    botoes = []
    game_finished = False

    # Botão "Jogar novamente"
    replay_button = pygame.Rect(largura//2 - 100, 450, 200, 50)

    # Variáveis para erro
    error_msg = ""
    error_timer = 0
    error_duration = 2000  # 2 segundos

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if show_question:
                    # Checar resposta
                    for rect, opcao in botoes:
                        if rect.collidepoint(event.pos):
                            if opcao == current_monster["resposta_certa"]:
                                current_monster["answered"] = True
                                show_question = False
                                current_monster = None
                                # Verifica se acabou o jogo
                                if all(m["answered"] for m in monsters):
                                    game_finished = True
                            else:
                                error_msg = "❌ Resposta incorreta! Tente novamente."
                                error_timer = pygame.time.get_ticks()
                elif game_finished:
                    # Se clicou no botão "Jogar novamente"
                    if replay_button.collidepoint(event.pos):
                        monsters = criar_monstros()
                        player_x, player_y = 625, 220
                        player_direction = "frente"
                        show_question = False
                        game_finished = False

        # Movimento só se o jogo não terminou
        if not show_question and not game_finished:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player_x -= player_speed
                player_direction = "esquerda"
            if keys[pygame.K_RIGHT]:
                player_x += player_speed
                player_direction = "direita"
            if keys[pygame.K_UP]:
                player_y -= player_speed
                player_direction = "costas"
            if keys[pygame.K_DOWN]:
                player_y += player_speed
                player_direction = "frente"

        # Limites do player
        player_x = max(0, min(player_x, largura - 50))
        player_y = max(0, min(player_y, altura - 50))
        player_rect = pygame.Rect(player_x, player_y, 50, 50)

        # Fundo
        tela.blit(terreno, (0, 0))
        tela.blit(casa, (0, 0))

        # Player
        tela.blit(player_images[player_direction], (player_x, player_y))

        # Mostra monstros
        for m in monsters:
            if not m["answered"]:
                tela.blit(m["image"], m["rect"].topleft)

        # Colisão ativa pergunta
        if not show_question and not game_finished:
            for m in monsters:
                if not m["answered"] and player_rect.colliderect(m["rect"]):
                    current_monster = m
                    botoes = [(pygame.Rect(150, 200 + i*60, 300, 40), opcao) 
                              for i, opcao in enumerate(m["opcoes"])]
                    show_question = True
                    break

        # Pergunta ativa
        if show_question and current_monster:
            pygame.draw.rect(tela, (20, 20, 20), (100, 100, 600, 400))
            txt_surface = fonte.render(current_monster["pergunta"], True, WHITE)
            tela.blit(txt_surface, (150, 130))
            for rect, opcao in botoes:
                pygame.draw.rect(tela, BLUE, rect)
                txt_surface = fonte.render(opcao, True, WHITE)
                tela.blit(txt_surface, (rect.x+10, rect.y+5))

            # Mensagem de erro se existir
            if error_msg and pygame.time.get_ticks() - error_timer < error_duration:
                err_surface = fonte.render(error_msg, True, RED)
                tela.blit(err_surface, (largura//2 - err_surface.get_width()//2, 500))
            else:
                error_msg = ""  # limpa msg após expirar

        # Tela final
        if game_finished:
            pygame.draw.rect(tela, (0, 100, 0), (150, 300, 500, 80))
            end_text = fonte.render("🎉 Parabéns! Você concluiu o jogo! 🎉", True, WHITE)
            tela.blit(end_text, (largura//2 - end_text.get_width()//2, 320))

            # Botão "Jogar novamente"
            pygame.draw.rect(tela, GREEN, replay_button)
            replay_text = fonte.render("Jogar novamente", True, WHITE)
            tela.blit(replay_text, (replay_button.centerx - replay_text.get_width()//2,
                                    replay_button.centery - replay_text.get_height()//2))

        pygame.display.flip()
        clock.tick(60)
