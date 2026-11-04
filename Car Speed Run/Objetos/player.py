# ===== IMPORTAÇÕES =====
import pygame
from pygame.locals import *

from main_config import DIM_OBJETOS, POS_OBJETOS
from Image.imagens import OBJETOS
from tuning import VELOCIDADES, VARIAVEIS_DE_CONTROLE, CONTADORES, MULTIPLICADORES, HP

from assets import carregar_imagem, carregar_sons
from Sound.music_and_sfx import EFEITOS

# ===== INICIANDO O PYGAME =====
pygame.init()


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        # Importando a Imagem do Player e Redimencinando ela
        self.player_img = carregar_imagem(OBJETOS["PLAYER"])
        self.player_img = pygame.transform.scale(self.player_img, (DIM_OBJETOS["DIM_PLAYER"]["WIDTH"],
                                                                   DIM_OBJETOS["DIM_PLAYER"]["HEIGHT"]))

        self.mask = pygame.mask.from_surface(self.player_img) # CRIANDO UMA "MASCARA" PARA COLIDIR PIXEL X PIXEL

        # Transformando a imagem em um retângulo e Atribuindo a sua posição inicial
        self.rect = self.player_img.get_rect()

        # Definindo em quantos pixel por segundo a imagem vai se deslocar pela tela

        self.taxa_acelera_x = VELOCIDADES["AUMENTO_VEL_X_PLAYER"]
        self.vel_max_x = VELOCIDADES["VELOCIDADE_X_MAX_PLAYER"]

        # Definindo os Estados do Jogador
        self.estadosPlayer = {
            "NO_CHAO":      "no chao",
            "NO_AR":        "no ar",
            "GIRANDO":      "girando",
        }

        # Variáveis de estado
        self.duracao_giro = VARIAVEIS_DE_CONTROLE["DURACAO_GIRO_PLAYER"]

        # Variáveis de HP do Player
        self.vida_max = HP["VIDA_MAX_PLAYER"]
        self.regen_rate = HP["TAXA_GANHO_VIDA"] # regenera 0.5 por frame sem colidir com o gelo-baiano
        self.perda_rate = HP["TAXA_PERDA_VIDA"] # perde 2 por frame colidido com o gelo-baiano
        self.largura_barra_vida = None

        self.som_pulo = carregar_sons(EFEITOS["PULO"])

        self.reset() # para não duplicar variáveis
    # __init__()

    def processar_eventos(self, eventos):
        for event in eventos:

            if event.type == KEYDOWN:
                if event.key == K_SPACE or event.key == K_UP or event.key == K_w:
                    self.pular()
    # processar_eventos()

    def update(self):

        # Definindo comportamentos por Estado do Player
        if self.estado_atual == self.estadosPlayer["NO_CHAO"]:
            self.update_noChao()
        elif self.estado_atual == self.estadosPlayer["NO_AR"]:
            self.update_noAr()
        elif self.estado_atual == self.estadosPlayer["GIRANDO"]:
            self.update_girando()
    # update()

    def update_noChao(self):
        # Acelerando o movimento Horizontal do jogador
        self.velocidade += self.taxa_acelera_x
        if self.velocidade >= self.vel_max_x:
            self.velocidade = self.vel_max_x

        # Regenerando a vida do Player
        self.vida = min(self.vida + self.regen_rate, self.vida_max)

        self.ja_pulou = False # verificando se o player pulou ou está no chão

        # Atualizando a barra de vida
        self.largura_barra_vida = int(HP["LARGURA_BARRA_VIDA"] * (self.vida / self.vida_max)) # Diminuindo a vida

        # Gerando Movimento no Player
        button = pygame.key.get_pressed()  # Se eu manter pressionado uma tecla do teclado

        if button[K_RIGHT] or button[K_d]:  # E essa tecla for --> ou "d"
            self.rect.x += self.velocidade  # mova o player para a direita

        if button[K_LEFT] or button[K_a]:  # E essa tecla for <-- ou "a"
            self.rect.x -= self.velocidade  # mova o player para esquerda

        # Limitando o Movimento do Player
        if self.rect.x <= VARIAVEIS_DE_CONTROLE["LIMITE_ESQUEDO_PISTA"]:  # bloqueia o movimento no lado esquedo
            self.rect.x = VARIAVEIS_DE_CONTROLE["LIMITE_ESQUEDO_PISTA"]

        if self.rect.x >= VARIAVEIS_DE_CONTROLE["LIMITE_DIREITO_PISTA"]:  # bloqueia o movimento no lado direito
            self.rect.x = VARIAVEIS_DE_CONTROLE["LIMITE_DIREITO_PISTA"]
    # update_normal()

    def update_girando(self):
        '''A animação de carro girando após colidir com óleo'''
        self.timer_giro += CONTADORES["INCREMENTO_TIMER_GIRO"]
        self.angulo_giro = (self.angulo_giro + CONTADORES["INCREMENTO_ANGULO_GIRO"]) % MULTIPLICADORES["MULT_ANGULO"] # player gira 15° por frame

        # fazendo o player "despencar após sair da pista
        if self.rect.x < VARIAVEIS_DE_CONTROLE["LIMITE_QUEDA_PISTA"]:
            self.rect.x += CONTADORES["INCREMENTO_DESLOC_X_PLAYER"]  # Faz o Player deslizar para fora da Pista

        else:
            self.rect.y += CONTADORES["INCREMENTO_DESLOC_Y_PLAYER"]

        if self.timer_giro >= self.duracao_giro:
            # Indicativo para a fase que o player parou de girar
            self.giro_terminou = True
    # upadate_girando()

    def update_noAr(self):
        # SOBE ATÉ A ALTURA MAXIMA DEPOIS DESCE
        if self.altura_pulo < VARIAVEIS_DE_CONTROLE["ALTURA_MAX_PULO"] and not self.ja_pulou:
            self.rect.y -= VELOCIDADES["VELOCIDADE_PULO"]
            self.altura_pulo += VELOCIDADES["VELOCIDADE_PULO"]

        else: # DESCE ATÉ A POSIÇÃO INICIAL DO PLAYER
            self.ja_pulou = True
            self.rect.y += VELOCIDADES["VELOCIDADE_PULO"]
            self.altura_pulo -= VELOCIDADES["VELOCIDADE_PULO"]


            # DEFINE QUANDO VOLTOU PARA O CHÃO
            if self.altura_pulo <= VARIAVEIS_DE_CONTROLE["ALTURA_INICIAL"]:
                self.rect.y = POS_OBJETOS["POS_PLAYER"]["Y"]
                self.estado_atual = self.estadosPlayer["NO_CHAO"]
    # update_noAr()

    def desenhar(self, surface):
        # Verificando se o playr está girando
        if self.estado_atual == self.estadosPlayer["GIRANDO"]:
            # Girando a imagem pelo Âgulo atual                     "-" gira horário
            img_rodando = pygame.transform.rotate(self.player_img, - self.angulo_giro)

            # o rotate() muda o tamanho da imagem sendo necessário recentralizar ela
            rect_img_rodando = img_rodando.get_rect(center=self.rect.center) # pegando o centro da imagem original

            # desenhando a imagem rodando
            surface.blit(img_rodando, rect_img_rodando)

        elif self.estado_atual == self.estadosPlayer["NO_AR"]:
            # Escala baseada na altura do pulo
            escala = 1.0 + (self.altura_pulo / VARIAVEIS_DE_CONTROLE["ALTURA_MAX_PULO"]) * 0.3

            # 1.0 no chão, 0.7 no topo do pulo
            largura = int(DIM_OBJETOS["DIM_PLAYER"]["WIDTH"] * escala)
            altura = int(DIM_OBJETOS["DIM_PLAYER"]["HEIGHT"] * escala)

            img_escalada = pygame.transform.scale(self.player_img, (largura, altura))

            rect_escalado = img_escalada.get_rect(center=self.rect.center)

            surface.blit(img_escalada, rect_escalado)

        else:
            # 1.0 DESENHANDO O PLAYER NA SUPERFÍCIE
            surface.blit(self.player_img, (self.rect.x, self.rect.y))
    # desenhar()

    def pular(self):
        if self.estado_atual == self.estadosPlayer["NO_CHAO"]:
            self.estado_atual = self.estadosPlayer["NO_AR"]
            self.altura_pulo = 0
            self.som_pulo.play()
    # pular()

    def reset(self):
        # Reset os atributos do player
        self.rect.x = POS_OBJETOS["POS_PLAYER"]["X"]
        self.rect.y = POS_OBJETOS["POS_PLAYER"]["Y"]
        self.velocidade = VELOCIDADES["VELOCIDADE_X_PLAYER"]
        self.vida = HP["VIDA_PLAYER"]
        self.estado_atual = self.estadosPlayer["NO_CHAO"]
        self.angulo_giro = VARIAVEIS_DE_CONTROLE["ANGULO_GIRO_PLAYER"]
        self.timer_giro = VARIAVEIS_DE_CONTROLE["TIMER_GIRO_PLAYER"]
        self.giro_terminou = False
        self.ja_trocou = False # Verifica se após o player colidir com o oleo e girar se ele já tentou mudar a Fase para Game Over
        self.largura_barra_vida = int(HP["LARGURA_BARRA_VIDA"] * (self.vida / self.vida_max))
        self.ja_pulou = False # flag para verificar se o botão de pulo foi acionado
        self.subida_penhasco = False # flag para verificar se o player começou a interagir com o penhasco
        self.altura_pulo = VARIAVEIS_DE_CONTROLE["ALTURA_INICIAL"]
    # reset()
# Player:
