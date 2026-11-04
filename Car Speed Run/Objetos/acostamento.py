# ===== IMPORTAÇÕES =====
import pygame

from main_config import SCREEN_CONFIG, DIM_OBJETOS, POS_OBJETOS
from tuning import VARIAVEIS_DE_CONTROLE, MULTIPLICADORES

from assets import carregar_imagem
from Image.imagens import CENARIO


class Acostamento(pygame.sprite.Sprite):
    """Arbusto lateral — só cenário, sem colisão"""

    def __init__(self, x, posicao_na_fila=0, estacao="PRIMAVERA"):
        super().__init__()
        self.image = carregar_imagem(CENARIO[f"ACOSTAMENTO_{estacao}"])
        self.image = pygame.transform.scale(self.image, (DIM_OBJETOS["DIM_ACOSTAMENTO"]["WIDTH"],
                                                         DIM_OBJETOS["DIM_ACOSTAMENTO"]["HEIGHT"]))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = POS_OBJETOS["POS_ACOSTAMENTO"]["Y"] + (posicao_na_fila * VARIAVEIS_DE_CONTROLE["ESPACO_ENTRE_ACOSTAMENTO"])
    # __init__()

    def update(self, velocidade_scroll):
        self.rect.y += velocidade_scroll
        if self.rect.top > SCREEN_CONFIG["HEIGHT_PISTA"]:
            self.rect.y -= VARIAVEIS_DE_CONTROLE["QTDE_ACOSTAMENTO"] * VARIAVEIS_DE_CONTROLE["ESPACO_ENTRE_ACOSTAMENTO"]
    # upadate()
# Acostamento: