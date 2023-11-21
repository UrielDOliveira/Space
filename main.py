import pygame
from tkinter import simpledialog

pygame.init()

largura = 1280
altura = 720
executando = True
janela = pygame.display.set_mode((largura, altura))
icone = pygame.image.load('space.png')
fundo = pygame.image.load("fundo.jpg").convert()
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
            nome = simpledialog.askstring("Space", "Nome da Estrela")
            if nome is None:
                nome = "desconhecido"
            estrelas.append((nome, pos))
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                executando = False

    janela.blit(fundo, (0, 0))  # Desenha a imagem de fundo

    for nome, posicao in estrelas:
        pygame.draw.circle(janela, BRANCO, posicao, 10)
        texto = f"{nome} ({posicao[0]}, {posicao[1]})"
        texto_surface = fonte.render(texto, True, BRANCO)
        posicao_texto = texto_surface.get_rect(center=(posicao[0], posicao[1] - 20))
        janela.blit(texto_surface, posicao_texto)  # Desenha o nome da estrela

    pygame.display.update()

pygame.mixer.music.stop()
pygame.quit()
