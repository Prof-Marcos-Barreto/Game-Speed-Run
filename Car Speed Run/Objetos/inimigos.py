# ===== IMPORTAÇÕES =====
import pygame

from main_config import SCREEN_CONFIG, DIM_OBJETOS, POS_OBJETOS
from Image.imagens import OBJETOS
from tuning import VELOCIDADES

from Sound.music_and_sfx import EFEITOS

from assets import carregar_imagem, carregar_sons

from random import randint


# ===== INICIANDO O PYGAME =====
pygame.init()


class Inimigos(pygame.sprite.Sprite):

    def __init__(self, faixa=None):
        super().__init__()

        # Importando a Lista de Imagens dos Inimigos e Redimencinando ela com seu Index
        self.index = randint(0, len(OBJETOS["INIMIGOS"]) - 1) # sorteando os inimigos
        self.lista_inimigos = OBJETOS["INIMIGOS"]

        imagem_escolhida = self.lista_inimigos[self.index]
        self.image = carregar_imagem(imagem_escolhida)
        self.image = pygame.transform.scale(self.image, (DIM_OBJETOS["DIM_INIMIGOS"]["WIDTH"],
                                                         DIM_OBJETOS["DIM_INIMIGOS"]["HEIGHT"]))

        self.mask = pygame.mask.from_surface(self.image)

        # Transformando a imagem em um retângulo e Atribuindo a sua posição inicial
        self.rect = self.image.get_rect()

        # Preparando para o sorteio de spawn
        if faixa is None:
            faixa = randint(0, 1)

        self.rect.x = POS_OBJETOS["POS_INIMIGOS"]["X"][faixa]
        self.rect.y = POS_OBJETOS["POS_INIMIGOS"]["Y"]

        # Definindo em quantos pixel por segundo a imagem vai se deslocar pela tela
        self.velocidade = VELOCIDADES["VELOCIDADE_Y_INIMIGOS"]
        self.taxa_aumento_vel = VELOCIDADES["AUMENTO_VEL_Y_INIMIGOS"]
        self.velocidade_max = VELOCIDADES["VELOCIDADE_Y_MAX_INIMIGOS"]

        # Flag para verificar se o efeito sonoro já tocou
        self.som_tocado = False
    # __init__()

    def update(self):
        # Movimentando o inimigo
        self.rect.y += self.velocidade
        self.velocidade += self.taxa_aumento_vel

        if self.velocidade >= self.velocidade_max:
            self.velocidade = self.velocidade_max

        # Atualizando o Inimigo

        # Atualizando a posição do Inimigo

        # Elimenando os inimigos após saírem da tela
        if self.rect.top > SCREEN_CONFIG["HEIGHT_PISTA"]:
            self.kill()
    # update()

    def ao_colidir(self):
        if not self.som_tocado:
            carregar_sons(EFEITOS["EXPLOSAO"]).play()
            self.som_tocado = True
    # ao_colidir()
# Inimigos:
