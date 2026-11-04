# ===== IMPORTAÇÕES =====
import pygame

from main_config import SCREEN_CONFIG, DIM_OBJETOS, POS_OBJETOS
from Image.imagens import OBJETOS

from Sound.music_and_sfx import EFEITOS

from assets import carregar_imagem, carregar_sons

from random import randint


# ===== INICIANDO O PYGAME =====
pygame.init()


class Obstaculos(pygame.sprite.Sprite):

    def __init__(self, faixa=None):
        super().__init__()

        # Importando a Lista de Imagens dos Obstáculos e Redimencinando ela com seu Index
        self.index = randint(0, len(OBJETOS["OBSTACULOS"]) - 1) # sorteando os Obstáculos
        self.lista_obstaculos = OBJETOS["OBSTACULOS"]

        imagem_escolhida = self.lista_obstaculos[self.index]
        self.image = carregar_imagem(imagem_escolhida)
        self.image = pygame.transform.scale(self.image, (DIM_OBJETOS["DIM_OBSTACULOS"]["WIDTH"],
                                                         DIM_OBJETOS["DIM_OBSTACULOS"]["HEIGHT"]))

        self.mask = pygame.mask.from_surface(self.image)

        # Transformando a imagem em um retângulo e Atribuindo a sua posição inicial
        self.rect = self.image.get_rect()

        # Preparando para o sorteio de spawn
        if faixa is None:
            faixa = randint(0, 2)

        self.rect.x = POS_OBJETOS["POS_OBSTACULOS"]["X"][faixa]
        self.rect.y = POS_OBJETOS["POS_OBSTACULOS"]["Y"]

        # Flag para verificar se o efeito sonoro já tocou
        self.som_tocado = False
    # __init__()

    def update(self, velocidade_scroll):
        # Movimentando o obstáculo
        self.rect.y += velocidade_scroll

        # Elimenando os Obstáculos após saírem da tela
        if self.rect.top > SCREEN_CONFIG["HEIGHT_PISTA"]:
            self.kill()
    # update()

    def ao_colidir(self):
        carregar_sons(EFEITOS["EXPLOSAO"]).play()
        self.som_tocado = True
    # ao_colidir()
# Obstaculos:
