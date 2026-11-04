# ===== IMPORTAÇÕES =====
import pygame

from main_config import SCREEN_CONFIG, DIM_OBJETOS, POS_OBJETOS
from Image.imagens import OBJETOS

from Sound.music_and_sfx import EFEITOS

from assets import carregar_imagem, carregar_sons


# ===== INICIANDO O PYGAME =====
pygame.init()


class Penhasco(pygame.sprite.Sprite):

    def __init__(self, estacao="PRIMAVERA"):
        super().__init__()

        self.image = carregar_imagem(OBJETOS["PENHASCO"][f'PENHASCO_{estacao}'])
        self.image = pygame.transform.scale(self.image, (DIM_OBJETOS["DIM_PENHASCO"]["WIDTH"],
                                                         DIM_OBJETOS["DIM_PENHASCO"]["HEIGHT"]))

        # Transformando a imagem em um retângulo e Atribuindo a sua posição inicial
        self.rect = self.image.get_rect()

        # Preparando para o sorteio de spawn

        self.rect.x = POS_OBJETOS["POS_PENHASCO"]["X"]
        self.rect.y = POS_OBJETOS["POS_PENHASCO"]["Y"]

        # Retângulos de colisão para habilitar região de pulo

        # Linha superior — mata se no chão
        self.rect_bloqueia_pulo = pygame.Rect(
            self.rect.x,
            self.rect.y + 150,
            self.rect.width,
            150
        )
    # __init__()

    def update(self, velocidade_scroll):
        # Movimentando o obstáculo
        self.rect.y += velocidade_scroll
        self.rect_bloqueia_pulo.y += velocidade_scroll

        # Elimenando os Obstáculos após saírem da tela
        if self.rect.top > SCREEN_CONFIG["HEIGHT_PISTA"]:
            self.kill()
    # update()

    def ao_colidir(self):
        pass
    # ao_colidir()
# Penhasco: