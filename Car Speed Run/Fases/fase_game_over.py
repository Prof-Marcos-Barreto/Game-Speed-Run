# ===== IMPORTAÇÕES =====
import pygame
from pygame.locals import *

from main_config import SCREEN_CONFIG, CORES, GAMESTATE, FONTES
from Sound.music_and_sfx import MÚSICAS, EFEITOS

from main_metodos import renderiza_text, desenha_opcoes_Menu

from Fases.construtor_fases import Fase

# ===== INICIANDO O PYGAME =====
pygame.init()


class GameOver(Fase):
    """Fase do Menu Principal"""

    def __init__(self):
        super().__init__(CORES['PRETO'], GAMESTATE["GAMEOVER"])

        # Variáveis de controle de opções
        self.opcoes = ["RESTART", "MENU"]
        self.opcao_selecionada = 0
    #__init__()

    def iniciar(self):
        super().iniciar()
        # resentando a opção de seleção
        self.opcao_selecionada = 0
    # iniciar()

    def processar_eventos(self, eventos):
        for event in eventos:
            if event.type == QUIT:
                return False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.proxima_fase = GAMESTATE["MENU"]

                if event.key == K_UP:
                    self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes) # Diminue o valor do indice da opçao selecionada

                elif event.key == K_DOWN:
                    self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes) # Aumenta o valor do índice da opção selecionada

                if event.key == K_RETURN: # Se eu apertar a tecla ENTER

                    if self.opcao_selecionada == 0: # Na primeira opção da lista de opções
                        self.proxima_fase = GAMESTATE["FASE1"] # Inicia Novamente a fase do jogo

                    elif self.opcao_selecionada == 1:
                        self.proxima_fase = GAMESTATE["MENU"] # Volte para o Menu do Jogo

        return True
    # processar_eventos()

    def desenhar(self, screen):
        # Preenche o fundo
        self.surface.fill(self.cor_fundo)

        # 1.0 Título da Tela
        renderiza_text(True, self.surface, FONTES["TITULO"], 50, "GAME OVER", CORES["VERMELHO"],
                       SCREEN_CONFIG["CENTER_X"], 10, "MID_TOP")

        # 2.0 Opções de Game Over
        desenha_opcoes_Menu(True, self.surface, self.opcoes, FONTES["OPCAO"], "VERMELHO","BRANCO", self.opcao_selecionada)

        screen.blit(self.surface, (0, 0))
    # desenhar()
# GameOver:
