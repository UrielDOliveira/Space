import pygame
icone = ('icone.ico')

def carregar_imagem(icone):
    try:
        imagem = pygame.image.load(icone)
        return imagem
    except pygame.error:
        print("Erro ao carregar a imagem:", icone)
        return None
