import pygame

# Loop primeira fase
def firstScreen(tela, fonte):
    # Tamanho Tela
    largura, altura = 800, 600

    # Cores
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    YELLOW = (255, 255, 100)
    BLUE = (100, 100, 255)
    RED = (255, 100, 100)
    GREEN = (100, 255, 100)

    # Jogador
    player = pygame.Rect(100, 100, 50, 50)
    player_color = BLACK
    player_speed = 5

    # Monstrinhos
    monsters = [
        {"rect": pygame.Rect(300, 200, 50, 50), "color": RED, "msg": "Está bravo? Respire fundo 3 vezes!"},
        {"rect": pygame.Rect(500, 300, 50, 50), "color": BLUE, "msg": "Triste? Que tal conversar com alguém?"},
        {"rect": pygame.Rect(200, 400, 50, 50), "color": YELLOW, "msg": "Está nervoso? Conte até 10 devagar."},
        {"rect": pygame.Rect(600, 150, 50, 50), "color": GREEN, "msg": "Ansioso? Pense em algo que te acalma."}
    ]

    # Mensagem atual
    current_msg = ""
    msg_timer = 0  # Timer para desaparecer a mensagem

    clock = pygame.time.Clock()

    running = True
    while running:
        tela.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False  # Sai da fase

        # Movimentação do jogador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: player.x -= player_speed
        if keys[pygame.K_RIGHT]: player.x += player_speed
        if keys[pygame.K_UP]: player.y -= player_speed
        if keys[pygame.K_DOWN]: player.y += player_speed

        # Desenhar jogador
        pygame.draw.rect(tela, player_color, player)

        # Verificar colisões com monstrinhos
        for m in monsters:
            pygame.draw.rect(tela, m["color"], m["rect"])
            if player.colliderect(m["rect"]):
                current_msg = m["msg"]
                msg_timer = pygame.time.get_ticks()

        # Exibir mensagem
        if current_msg and pygame.time.get_ticks() - msg_timer < 4000:
            text_surface = fonte.render(current_msg, True, BLACK)
            tela.blit(text_surface, (largura //2 - text_surface.get_width()//2, 20))
        elif pygame.time.get_ticks() - msg_timer >= 4000:
            current_msg = ""

        pygame.display.flip()
        clock.tick(60)

