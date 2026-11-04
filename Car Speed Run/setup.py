"""
Módulo responsável por inicializar o pygame e criar os recursos globais:
- Display (tela)
- Clock (controle de FPS)
- Mixer (áudio)

Deve ser chamado UMA VEZ no início do jogo, antes de criar qualquer fase.
"""

# ===== IMPORTAÇÕES =====
import pygame
from main_config import SCREEN_CONFIG


def inicializa_pygame():
    """
    -> Inicia o pygame, ccria uma tela eo clock
    :return: uma Tupla: (screen, Clock)
    """

    # ===== INICIALIZAÇÃO =====

    # 1. INICIALIZAÇÃO DO PYGAME
    pygame.init()

    # 1.1 INICIALIZAÇÃO DO MIXER
    pygame.mixer.init()

    # 2. CONFIGURAÇÕES BÁSICAS

    # 2.1 DIMENSIONANDO E NOMEANDO A TELA
    screen = pygame.display.set_mode((SCREEN_CONFIG['WIDTH'], SCREEN_CONFIG['HEIGHT']))
    pygame.display.set_caption(SCREEN_CONFIG['GAME_NAME'])

    # 3. RELÓGIO PARA CONTROLAR O FPS
    clock = pygame.time.Clock()

    return screen, clock
# inicializa_pygame()