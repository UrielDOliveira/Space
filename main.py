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
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
            
    pygame.display.update()

pygame.mixer.music.stop()
pygame.quit()
