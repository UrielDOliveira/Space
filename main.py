import pygame
from tkinter import simpledialog

pygame.init()

largura = 1280
altura = 720
executando = True
janela = pygame.display.set_mode((largura, altura))
icone = pygame.image.load('space.png')
fundo = pygame.image.load("fundo.jpg").convert()  # Carregar a imagem e convertê-la para um formato adequado
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
musica = pygame.mixer.music.load("Musica.mp3")
fonte = pygame.font.Font(None, 24)
estrelas = []

pygame.display.set_caption("Marcador de Estrelas")
pygame.mixer.init()
pygame.mixer.music.play(-1)
pygame.display.set_icon(icone)

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        elif evento.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("Space", "Nome da Estrela")
            print(item)
            if item is None:
                item = "desconhecido" + str(pos)
            # estrelas[item] = pos
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                executando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            posicao = pygame.mouse.get_pos()
            nome = input("Digite o nome da estrela: ")
            estrelas.append((nome, posicao))

    janela.blit(fundo, (0, 0))  # Desenhar a imagem de fundo no início do loop
    for nome, posicao in estrelas:
        pygame.draw.circle(janela, BRANCO, posicao, 10)
        texto_surface = fonte.render(nome, True, BRANCO)
        posicao_texto = texto_surface.get_rect(center=(posicao[0], posicao[1] - 20))
        janela.blit(texto_surface, posicao_texto)  # Desenhar o texto no centro da estrela

    pygame.display.update()

pygame.mixer.music.stop()
pygame.quit()
