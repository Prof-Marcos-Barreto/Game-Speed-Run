# ===== IMPORTAÇÕES =====
import pygame

from main_config import SCREEN_CONFIG, DIM_OBJETOS, POS_OBJETOS
from Image.imagens import OBJETOS
from tuning import VARIAVEIS_DE_CONTROLE

from Sound.music_and_sfx import EFEITOS

from assets import carregar_imagem, carregar_sons


# ===== INICIANDO O PYGAME =====
pygame.init()


class Gelo_Baiano(pygame.sprite.Sprite):
    """Fase do Menu Principal"""

    def __init__(self, posicao_na_fila=0):
        super().__init__()

        # Importando a Lista de Imagens do GELO-BAIANO e Redimencinando ela

        self.image = carregar_imagem(OBJETOS["GELO-BAIANO"])
        self.image = pygame.transform.scale(self.image, (DIM_OBJETOS["DIM_GELO-BAIANO"]["WIDTH"],
                                                         DIM_OBJETOS["DIM_GELO-BAIANO"]["HEIGHT"]))

        self.mask = pygame.mask.from_surface(self.image)

        # Transformando a imagem em um retângulo e Atribuindo a sua posição inicial
        self.rect = self.image.get_rect()

        self.rect.x = POS_OBJETOS["POS_GELO-BAIANO"]["X"]    # empilha uma fileira: disância de 50 pix entre eles
        self.rect.y = POS_OBJETOS["POS_GELO-BAIANO"]["Y"] + (posicao_na_fila * VARIAVEIS_DE_CONTROLE["ESPACO_ENTRE_GELO_BAIANO"])
    # __init__()

    def update(self, velocidade_scroll):
        # Movimentando o GELO-BAIANO
        self.rect.y += velocidade_scroll

        # Elimenando o ÓLEO após saírem da tela
        if self.rect.top > SCREEN_CONFIG["HEIGHT_PISTA"]:
            self.rect.top -= VARIAVEIS_DE_CONTROLE["QTDE_GELO_BAIANO_CRIADO"] * VARIAVEIS_DE_CONTROLE["ESPACO_ENTRE_GELO_BAIANO"]
    # update()
# Gelo_Baiano:
