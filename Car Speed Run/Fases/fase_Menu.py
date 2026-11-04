# ===== IMPORTAÇÕES =====
import pygame
from pygame.locals import *

from main_config import SCREEN_CONFIG, CORES, GAMESTATE, FONTES
from Sound.music_and_sfx import MÚSICAS, EFEITOS
from main_metodos import renderiza_text, desenha_opcoes_Menu
from tuning import CONTADORES

from assets import carregar_musicas, carregar_sons

from Fases.construtor_fases import Fase


# ===== INICIANDO O PYGAME =====
pygame.init()


class FaseMenu(Fase):
    """Fase do Menu Principal"""

    def __init__(self):
        super().__init__(CORES['PRETO'], GAMESTATE["MENU"])

        # Variáveis específicas do menu
        self.opcao_selecionada = 0
        self.opcoes = ["START", "OPÇÕES"]

        # Timer para criar um "dalay"
        self.esperando = False
        self.tempo_espera = CONTADORES["TEMPO_ESPERA_MENU"]
        self.duracao_espera = CONTADORES["DURACAO_ESPERA_MENU"] # representa 2s a 60FPS

        # Variáveis para fazer o nome mudar de cor
        self.flag_cor = False
        self.timer_cor = CONTADORES["TIMER_COR"]
        self.duracao_cor_on = CONTADORES["DURACAO_COR_ON"]
        self.duracao_cor_off = CONTADORES["DURACAO_COR_OFF"]
    # __init__()

    def processar_eventos(self, eventos):
        for event in eventos:
            if event.type == QUIT:
                return False

            if event.type == KEYDOWN:

                if event.key == K_UP:
                    self.opcao_selecionada = (self.opcao_selecionada - 1) % len(self.opcoes) # Diminue o valor do indice da opçao selecionada

                elif event.key == K_DOWN:
                    self.opcao_selecionada = (self.opcao_selecionada + 1) % len(self.opcoes) # Aumenta o valor do índice da opção selecionada

                elif event.key == K_RETURN:

                    if self.opcao_selecionada == 0:  # Iniciar jogo

                        # Confirmação Sonora Início da Fase 1
                        carregar_sons(EFEITOS["BT_START"]).play() # toca o som após clicar no START
                        pygame.mixer.music.stop() # desliga a música de fundo

                        # validando o tempo de espera pra transição de fase
                        self.esperando = True
                        self.tempo_espera = CONTADORES["TEMPO_ESPERA_MENU"]

                    elif self.opcao_selecionada == 1:
                        pass

        return True
    # processar_eventos()

    def atualizar(self):

        # criando o dalay da transição de fase
        if self.esperando:
            self.tempo_espera += CONTADORES["INCREMENTO_TEMPO_ESPERA_MENU"]
            if self.tempo_espera >= self.duracao_espera:
                self.esperando = False # reseta a espera da fase
                self.proxima_fase = GAMESTATE["FASE1"]

        # Timer para nome do jogo mudar de cor
        self.timer_cor += CONTADORES["INCREMENTO_COR"]
        if self.flag_cor and self.timer_cor >= CONTADORES["DURACAO_COR_ON"]:
            self.flag_cor = False
            self.timer_cor = 0

        elif not self.flag_cor and self.timer_cor >= CONTADORES["DURACAO_COR_OFF"]:
            self.flag_cor = True
            self.timer_cor = 0

    # atualizar()

    def desenhar(self, screen):
        # Preenche o fundo
        self.surface.fill(self.cor_fundo)

        # Título
        renderiza_text(True, self.surface, FONTES["TITULO"], 50, 'MENU', CORES['BRANCO'],
                       SCREEN_CONFIG["CENTER_X"], 10, "MID_TOP")

        # Nome do Jogo
        if self.flag_cor:
            renderiza_text(True, self.surface,  FONTES["TITULO"], 35, SCREEN_CONFIG["GAME_NAME"], CORES["AZUL"],
                           SCREEN_CONFIG["CENTER_X"], 150,  "MID_TOP")
        else:
            renderiza_text(True, self.surface, FONTES["TITULO"], 35, SCREEN_CONFIG["GAME_NAME"], CORES["VERMELHO"],
                           SCREEN_CONFIG["CENTER_X"], 150, "MID_TOP")

        # Opções
        desenha_opcoes_Menu(True, self.surface, self.opcoes, FONTES["OPCAO"], "VERDE", "BRANCO", self.opcao_selecionada)

        screen.blit(self.surface, (0, 0))
    # desenhar()
# FaseMenu:
