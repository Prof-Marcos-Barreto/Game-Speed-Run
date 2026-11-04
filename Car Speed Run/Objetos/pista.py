# ===== IMPORTAÇÕES =====
import pygame

from main_config import SCREEN_CONFIG, DIM_OBJETOS, POS_OBJETOS
from tuning import VARIAVEIS_DE_CONTROLE

from assets import carregar_imagem
from Image.imagens import CENARIO


class Pista(pygame.sprite.Sprite):
    """Pista — só cenário, sem colisão"""

    def __init__(self, posicao_na_fila=0, estacao="PRIMAVERA"):
        super().__init__()
        self.image = carregar_imagem(CENARIO[f"PISTA_{estacao}"])
        self.image = pygame.transform.scale(self.image, (DIM_OBJETOS["DIM_PISTA"]["WIDTH"],
                                                         DIM_OBJETOS["DIM_PISTA"]["HEIGHT"]))

        self.rect = self.image.get_rect()
        self.rect.x = POS_OBJETOS["POS_PISTA"]["X"]
        self.rect.y = POS_OBJETOS["POS_PISTA"]["Y"] + (posicao_na_fila * SCREEN_CONFIG["HEIGHT_PISTA"])
    # __init__()

    def update(self, velocidade_scroll):
        self.rect.y += velocidade_scroll
        if self.rect.top > SCREEN_CONFIG["HEIGHT_PISTA"]:
            self.rect.y -= VARIAVEIS_DE_CONTROLE["QTDE_PISTA"] * SCREEN_CONFIG["HEIGHT_PISTA"]
    # upadate()
# Pista: