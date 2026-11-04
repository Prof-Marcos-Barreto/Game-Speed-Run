# ===== IMPORTAÇÕES =====
import pygame

from main_config import SCREEN_CONFIG, DIM_OBJETOS, POS_OBJETOS
from Image.imagens import OBJETOS

from Sound.music_and_sfx import EFEITOS

from assets import carregar_imagem, carregar_sons

from random import randint


# ===== INICIANDO O PYGAME =====
pygame.init()


class Oleo(pygame.sprite.Sprite):

    def __init__(self, faixa=None):
        super().__init__()

        # Importando a Lista de Imagens do Oleo e Redimencinando ela

        self.image = carregar_imagem(OBJETOS["OLEO"])
        self.image = pygame.transform.scale(self.image, (DIM_OBJETOS["DIM_OLEO"]["WIDTH"],
                                                         DIM_OBJETOS["DIM_OLEO"]["HEIGHT"]))

        self.mask = pygame.mask.from_surface(self.image)

        # Transformando a imagem em um retângulo e Atribuindo a sua posição inicial
        self.rect = self.image.get_rect()

        # Preparando para o sorteio de spawn
        if faixa is None:
            faixa = randint(0, 2)

        self.rect.x = POS_OBJETOS["POS_OLEO"]["X"][faixa]
        self.rect.y = POS_OBJETOS["POS_OLEO"]["Y"]

        # Flag para verificar se o efeito sonoro já tocou
        self.som_tocado = False
    # __init__()

    def update(self, velocidade_scroll):
        # Movimentando o ÓLEO
        self.rect.y += velocidade_scroll

        # Elimenando o ÓLEO após saírem da tela
        if self.rect.top > SCREEN_CONFIG["HEIGHT_PISTA"]:
            self.kill()
    # update()

    def ao_colidir(self):
        if not self.som_tocado:
            carregar_sons(EFEITOS["DERRAPAGEM"]).play()
            self.som_tocado = True
    # ao_colidir()
# Oleo:
