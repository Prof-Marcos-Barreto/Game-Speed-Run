# ===== IMPORTAÇÕES =====
import pygame
from pygame.locals import *

from main_config import SCREEN_CONFIG, CORES, GAMESTATE, FONTES, POS_OBJETOS
from Image.imagens import CENARIO
from Sound.music_and_sfx import MÚSICAS, EFEITOS
from assets import carregar_musicas, carregar_imagem

from record import carregar, salvar
from main_metodos import renderiza_text
from tuning import VELOCIDADES, CONTADORES, MULTIPLICADORES, LIMITADORES, POS_INICIAIS, HP, SPAWNS,VARIAVEIS_DE_CONTROLE
from spawn import sortear_padrao, criar_objetos_do_padrao

from Fases.construtor_fases import Fase

from Objetos.player import Player
from Objetos.gelo_baiano import Gelo_Baiano
from Objetos.penhasco import Penhasco
from Objetos.acostamento import Acostamento
from Objetos.pista import Pista

# ===== INICIANDO O PYGAME =====
pygame.init()

# TODO: ajuste fino ========== ATENÇÃO!!! ==========
# - intervalo de spawn
# - velocidades (pista, inimigo)
# - sincronizar velocidades entre inimigo e scroll
# - Criar uma fase Pai para receber o player, inimigos e obstáculos como é com as fases
# - Trocar nos dicionários de imagens a importação pelo caminho!!!
# - Criar canais de músicas quando for implementar as transições de estação das pistas para por músicas idependendtes
# TODO: cortar/juntar música pra ficar mais constante + loop.


class Fase1(Fase):

    def __init__(self):
        super().__init__(CORES['AMARELO'], GAMESTATE["FASE1"])

        # 1.0 ===== VARIÁVEIS PARA O BACKGROUND =====
            # 1.1 Carregando Imagem da Pista
        self.pista = pygame.sprite.Group()

        # Variáveis para Definir a estção
        self.timer_estacao = 0
        self.duracao_estacao = 1200

        self.estacao =["PRIMAVERA", "VERAO", "OUTONO", "INVERNO"]
        self.index_estacao = 0
        self.estacao_atual = self.estacao[self.index_estacao]

        self.velocidade_scroll = VELOCIDADES["VELOCIDADE_SCROLL"] # velocidade inicial de descida da pista
        self.taxa_de_aumento_vel = VELOCIDADES["AUMENTO_VEL_SCROLL"]
        self.velocidade_max = VELOCIDADES["VELOCIDADE_MAX_SCROLL"]

            # 1.3 Linha de Chegada
        self.chegada = carregar_imagem(CENARIO["CHEGADA"])
        self.chegada = pygame.transform.scale(self.chegada, (SCREEN_CONFIG["WIDTH"] - SCREEN_CONFIG["HEIGHT_HUD"],
                                                             SCREEN_CONFIG["WIDTH"] / 4))
        self.chegada_rect = self.chegada.get_rect()
        self.chegada_rect.x = POS_INICIAIS["CHEGADA_X"]
        self.chegada_rect.y = POS_INICIAIS["CHEGADA_Y"]

            # 1.4 VARIÁVEIS DE SPAWNS DOS OBJETOS QUE COLIDEM COM O PLAYER
        self.timer_spawn_geral = CONTADORES["TIMER_SPAW_GERAL"]
        self.intervalo_spawn_geral = SPAWNS["INTERVALO_SPAW_GERAL"]

            #1.5 Criando e redimensionando o Acostamento
        self.acostamento_direito = pygame.sprite.Group()
        self.acostamento_esquerdo = pygame.sprite.Group()

        # 2.0 ===== VARIÁVEIS PARA O PERSONAGEM =====
        self.player = Player()

        # 3.0 ===== VARIÁVEIS PARA OS INIMIGOS =====
        self.inimigos = pygame.sprite.Group()

        # 4.0 ===== VARIÁVEIS PARA OS OBSTÁCULOS =====
        self.obstaculos = pygame.sprite.Group()

        # 5.0 ===== VARIÁVEIS PARA O ÓLEO =====
        self.oleo = pygame.sprite.Group()

        # 6.0 ===== VARIÁVEIS PARA O GELO-BAIANO =====
        self.gelo_baiano = pygame.sprite.Group()

        # 7.0 ===== VARIÁVEIS PARA O PENHASCO=====
        self.penhasco = pygame.sprite.Group()
        self.timer_penhasco = CONTADORES["TIMER_PENHASCO"]
        self.intervalo_penhasco = SPAWNS["INTERVALO_PENHASCO"]  # 15s
        self.cooldown_spawn = SPAWNS["COOLDOWN_SPAWN_PENHASCO"]
        self.duracao_cooldown = SPAWNS["DURACAO_COOLDOWN"]  # 3s

        # Flag de Debug - faz vizualizar as linhas do penhasco que colidem com o player e tira a colisão dos objetos com o player
        self.debug = False

        # 8.0 ===== VARIÁVEIS PARA CRIAR E SALVAR O SCORE =====
        self. score = CONTADORES["SCORE"]
        self.melhor_score = carregar() # Sempre irá abrir o arquivo e mostrar a melhor pontuação
    #__init__()

    def trocar_estacao(self):
        # Limpando o cenário atual
        self.acostamento_direito.empty()
        self.acostamento_esquerdo.empty()
        self.pista.empty()

        # Recriando o Cenário atual
        for i in range(VARIAVEIS_DE_CONTROLE["QTDE_PISTA"]):
            self.pista.add(Pista(posicao_na_fila=i, estacao=self.estacao_atual))

        for i in range(VARIAVEIS_DE_CONTROLE["QTDE_ACOSTAMENTO"]):
            self.acostamento_esquerdo.add(Acostamento(x=POS_OBJETOS["POS_ACOSTAMENTO"]["X_ESQUERDO"], posicao_na_fila=i, estacao=self.estacao_atual))
            self.acostamento_direito.add(Acostamento(x=POS_OBJETOS["POS_ACOSTAMENTO"]["X_DIREITO"], posicao_na_fila=i, estacao=self.estacao_atual))
    # troca_estacao()

    def iniciar(self):
        super().iniciar()
        # ===== CONFIGURAÇÕES DE RESET DA FASE =====
        # 1.0 ===== Inimigos
        self.inimigos.empty()

        # 2.0 ===== Cenário
            # 2.1 ===== resetando velocidade da pista
        self.velocidade_scroll = VELOCIDADES["VELOCIDADE_SCROLL"]

            # 2.2 Linha de chega
        self.chegada_rect.x = POS_INICIAIS["CHEGADA_X"]
        self.chegada_rect.y = POS_INICIAIS["CHEGADA_Y"] # POSIÇÃO INICIAL DA LINHA DE CHEGADA

            #2.3 reseta a estação Inicia sempre na Primavera
        self.index_estacao = 0
        self.timer_estacao = 0
        self.duracao_estacao = 1200
        self.estacao_atual = self.estacao[self.index_estacao]

            # 2.4 Limpando e recriando a pista
        self.pista.empty()
        for i in range(VARIAVEIS_DE_CONTROLE["QTDE_PISTA"]):
            self.pista.add(Pista(posicao_na_fila=i))

            # 2.5 Limpando e recriando o acostamento
        self.acostamento_direito.empty()
        self.acostamento_esquerdo.empty()

        for i in range(VARIAVEIS_DE_CONTROLE["QTDE_ACOSTAMENTO"]):
            self.acostamento_esquerdo.add(Acostamento(x=POS_OBJETOS["POS_ACOSTAMENTO"]["X_ESQUERDO"], posicao_na_fila=i))
            self.acostamento_direito.add(Acostamento(x=POS_OBJETOS["POS_ACOSTAMENTO"]["X_DIREITO"], posicao_na_fila=i))


        # 3.0 ===== Pontuação (score da fase)
        self.score = CONTADORES["SCORE"]

        # 4.0 ===== Player
        self.player.reset()

        # 5.0 ===== Obstáculos
        self.obstaculos.empty()

        # 6.0 ====== Óleo
        self.oleo.empty()

        # 7.0 ===== Gelo_baiano
        self.gelo_baiano.empty()
        for i in range(VARIAVEIS_DE_CONTROLE["QTDE_GELO_BAIANO_CRIADO"]):
            self.gelo_baiano.add(Gelo_Baiano(posicao_na_fila=i)) # cria 12 gelos-baiano na tela ao mesmo tempo

        # 8.0 ===== Penhasco
        self.penhasco.empty()
        self.timer_penhasco = CONTADORES["TIMER_PENHASCO"]
        self.cooldown_spawn = SPAWNS["COOLDOWN_SPAWN_PENHASCO"]

        # 9.0 ===== Spawn objetos que colidem com o player
        self.timer_spawn_geral = CONTADORES["TIMER_SPAW_GERAL"]

        # ===== CARREGANDO MÚSICAS E EFEITOS DO JOGO =====
        carregar_musicas(MÚSICAS["BG_VERAO"]) # Carregando a música de fundo
        pygame.mixer.music.play(-1)  # colocando a música de fundo para tocar infinitamente
        pygame.mixer.music.set_volume(0.5)  # Controla o volume da música de fundo

            # evitanodo que os efeitos sonoros toquem com o início da partida
        pygame.mixer.stop()
    #iniciar()

    def finalizar(self):
        super().finalizar()
        # 1.0 Salvando o score_máximo
        if self.score > self.melhor_score:
            self.melhor_score = self.score
            salvar(self.melhor_score)

        print(f'O Score final da partida: {self.score}\n'
              f'O Melhor Score é: {self.melhor_score}')

        # 2.0 Desligando a músuca de fundo da fase
        pygame.mixer.music.stop()
        self.player.som_pulo.stop() # faz o som de pula parar após uma colisão
    # finalizar()

    def processar_eventos(self, eventos):
        for event in eventos:
            if event.type == QUIT:
                return False

            if event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.proxima_fase = GAMESTATE["MENU"]

                elif event.key == K_SPACE or event.key == K_UP or event.key == K_w:
                    self.player.pular()

        return True
    # processar_eventos()

    def atualizar(self):

        # 1.0 ===== LÓGICA DE ATUALIZAÇÃO DO BACKGROUND =====
            # 1.1 Atualizando a velocidade de rolagem da tela
        self.velocidade_scroll += self.taxa_de_aumento_vel # Aumento gradativo da velocidade de descida até seu máximo
        if self.velocidade_scroll >= self.velocidade_max:
            self.velocidade_scroll = self.velocidade_max

            # 1.2 Atualizando a velocidade da pista
        self.pista.update(self.velocidade_scroll)

            # 1.3 atualizando a velocidade dos arbustos na tela
        self.acostamento_esquerdo.update(self.velocidade_scroll)
        self.acostamento_direito.update(self.velocidade_scroll)

        # TODO: Não esquecer de verficar a lógica da linha de chegado para não trava o movimento da pista! e por colisão com o player
        # TODO: A linha de chegada deve ser acionada depois de um limite de pontuação para chamar o fim do jogo NÃO ESQUECER!!!!
            # 1.4 Atualizando a Posição da Linha de Chegada
        if self.score >= LIMITADORES["SCORE_MAX"]: # --> AJUSTÁVEL
            self.chegada_rect.y += self.velocidade_scroll

        if self.chegada_rect.y >= SCREEN_CONFIG["HEIGHT_PISTA"] - VARIAVEIS_DE_CONTROLE["AJUSTE_POS_CHEGADA"]:
            self.chegada_rect.y = SCREEN_CONFIG["HEIGHT_PISTA"] - VARIAVEIS_DE_CONTROLE["AJUSTE_POS_CHEGADA"]

            # 1.5 Atualizando as Estações
        self.timer_estacao += 1
        if self.timer_estacao >= self.duracao_estacao: # Se o tempo da estação é = a duração da estação, então troque ela
            self.timer_estacao = 0  # reinicia o tempo da duração da estação atual
            self.index_estacao = (self.index_estacao + 1) % len(self.estacao)# Aumenta o indice da lista de estações para poder mudar a estação
            self.estacao_atual = self.estacao[self.index_estacao]
            self.trocar_estacao() # Muda a estação dos objetos da pista

        # 2.0 ===== LÓGICA DE ATUALIZAÇÃO PLAYER =====
            # 2.1 movimentação e bloqueio nas bordas
        self.player.update()

            # 2.2 Verificando se o Estado do Player é "GIRANDO"
        if self.player.estado_atual == self.player.estadosPlayer["GIRANDO"] and self.player.giro_terminou:
            if not self.player.ja_trocou: # flag para impedir a tentativa de mudar de fase mais de uma vez
                self.player.ja_trocou = True
                self.proxima_fase = GAMESTATE["GAMEOVER"]

        # ===== LÓGICA DE SPAWN DE OBJETOS QUE COLIDEM COM O PLAYER =====

            # Controlando o spawn do penhasco
        self.timer_penhasco += CONTADORES["INCREMENTO_SPAWN_PENHASCO"]
        if self.timer_penhasco >= self.intervalo_penhasco:
            self.timer_penhasco = CONTADORES["TIMER_PENHASCO"]
            self.penhasco.add(Penhasco(estacao=self.estacao_atual)) # Cria UM a cada 15s
            self.cooldown_spawn = self.duracao_cooldown

            # Controla a criação dos objetos que colidem com player
        if self.cooldown_spawn > SPAWNS["COOLDOWN_SPAWN_PENHASCO"]:
            self.cooldown_spawn -= CONTADORES["DECRESCIMO_COOLDOWN"] # em cooldown não spawna NADA
        else:
            self.timer_spawn_geral += CONTADORES["INCREMENTO_TIMER_SPAW_GERAL"]
            if self.timer_spawn_geral >= self.intervalo_spawn_geral:
                self.timer_spawn_geral = CONTADORES["TIMER_SPAW_GERAL"] # resetando o tempo de spawn para recomeçar a contagem e não bugar criando
                                            # muitos objetos ao mesmo tempo

                # Sosteando os objetos que colidem
                padrao = sortear_padrao()
                criar_objetos_do_padrao(padrao, {
                    "inimigo": self.inimigos,
                    "obstaculo": self.obstaculos,
                    "oleo": self.oleo
                })

        # 3.0 ===== LÓGICA DE ATUALIZAÇÃO INIMIGOS =====
            # 3.1 Movimentação, Reposicionamento e Exclusão dos Inimigos
        self.inimigos.update()

        # 4.0 ===== LÓGICA DE ATUALIZAÇÃO OBSTÁCULOS =====
            # 4.1 Movimentação, Reposicionamento e Exclusão dos Obstáculos
        self.obstaculos.update(self.velocidade_scroll)

        # 5.0 ===== LÓGICA DE ATUALIZAÇÃO DO ÓLEO =====
            # 5.1 Movimentação, Reposicionamento e Exclusão  do oleo
        self.oleo.update(self.velocidade_scroll)

        # 6.0 ===== LÓGICA DE ATUALIZAÇÃO DO GELO-BAIANO =====
            # 6.1 Movimentando Gelos-baiano
        self.gelo_baiano.update(self.velocidade_scroll)

        # 7.0 ===== LÓGICA DE ATUALIZAÇÃO DO PENHASCO =====
            # 7.1 Movimentando Penhasco
        self.penhasco.update(self.velocidade_scroll)

        # 8.0 ===== LÓGICA DE ATUALIZAÇÃO SCORE DO JOGO
            # 8.1 Aumentando o Score gradualmente
        self.score += int(self.velocidade_scroll) * MULTIPLICADORES["MULT_SCORE"]

            # 8.2 Simulando o velocímetro
        self.vel_display = int((self.velocidade_scroll / self.velocidade_max) * MULTIPLICADORES["MULT_VELOCIMETRO"])

        # 9.0 ===== LÓGICAS DE COLISÃO =====
        if not self.debug:
                # 9.1 Colisão Player com Inimigos
            if self.player.estado_atual == self.player.estadosPlayer["NO_AR"]\
                or self.player.estado_atual == self.player.estadosPlayer["NO_CHAO"] \
                or self.player.estado_atual == self.player.estadosPlayer["GIRANDO"]:
                # INDEPENDENTE DO ESTADO O PLAYER IRÁ COLIDIR COM OS INIMIGOS
                inimigo_atingido = pygame.sprite.spritecollide(self.player, self.inimigos, False, collided=pygame.sprite.collide_mask)
                if inimigo_atingido:
                    # gerencia o som de colisão para cada inimigo
                    for inimigo in inimigo_atingido:
                        inimigo.ao_colidir()
                    self.proxima_fase = GAMESTATE["GAMEOVER"]

                # 9.2 Colisão Player com Obstácuos
            if self.player.estado_atual == self.player.estadosPlayer["NO_AR"]:
                pass

            else: # Só vai haver colisão quando ele estiver no chão ou girando
                obstaculos_atingidos = pygame.sprite.spritecollide(self.player, self.obstaculos, False, collided=pygame.sprite.collide_mask)
                if obstaculos_atingidos:
                    for obstaculo in obstaculos_atingidos:
                        obstaculo.ao_colidir()
                    self.proxima_fase = GAMESTATE["GAMEOVER"]

                # 9.3 Colisão Player com o Óleo
            if self.player.estado_atual == self.player.estadosPlayer["NO_AR"]:
                pass
            else: # Só vai haver colisão quando ele estiver no chão ou girando
                oleo_atingido = pygame.sprite.spritecollide(self.player, self.oleo, False, collided=pygame.sprite.collide_mask)
                if oleo_atingido:
                    # gerencia o som de colisão para cada elemento oleo
                    for oleo in oleo_atingido:
                        oleo.ao_colidir()

                    # Mudando o estado do player
                    self.player.estado_atual = self.player.estadosPlayer["GIRANDO"]

                # 9.4 Colisão Player com gelo-baiano
            if self.player.estado_atual == self.player.estadosPlayer["NO_AR"]:
                pass
            else: # Só vai haver colisão quando ele estiver no chão ou girando
                gelo_baiano_atingido = pygame.sprite.spritecollide(self.player, self.gelo_baiano, False, collided=pygame.sprite.collide_mask)
                if gelo_baiano_atingido:
                    self.player.vida -= self.player.perda_rate
                    if self.player.vida <= HP["VIDA_MIN_PLAYER"]:
                        self.proxima_fase = GAMESTATE["GAMEOVER"]

                # 9.5 Colisão Player com penhasco
            for penhasco in self.penhasco:
                if (self.player.rect.colliderect(penhasco.rect_bloqueia_pulo)
                    and self.player.estado_atual != self.player.estadosPlayer["NO_AR"]):
                    self.proxima_fase = GAMESTATE["GAMEOVER"]
     # Atualizar()

    def desenhar(self, screen):
        # Preenche o fundo
        self.surface.fill(self.cor_fundo)

        # 1.0 ===== IMAGENS PARA O BACKGROUND =====
            # 1.1 Desenhando as Pistas na tela
        self.pista.draw(self.surface)

            # 1.2 desenhando o acostamento
        self.acostamento_esquerdo.draw(self.surface)
        self.acostamento_direito.draw(self.surface)

            # 1.3 Desenhando a Linha de Chegada
        self.surface.blit(self.chegada, (self.chegada_rect.x, self.chegada_rect.y))

        # 2.0 ===== DESENHANDO ELEMENTOS DO GELO-BAIANO =====
        self.gelo_baiano.draw(self.surface)

        # 3.0 ===== DESENHANDO ELEMENTOS DO PENHASCO =====
            # 3.1 linhas de colisão
        self.penhasco.draw(self.surface)
        # ===== DEBUG: desenhar rects de colisão do penhasco =====
        if self.debug:
            for penhasco in self.penhasco:
                pygame.draw.rect(self.surface, CORES["VERMELHO"], penhasco.rect_bloqueia_pulo, 1)  # contorno vermelhod

        # 4.0 ===== DESENHANDO ELEMENTOS DO ÓLEO
            # 4.1 Desenhando o Óleo
        self.oleo.draw(self.surface)

        # 5.0 ===== DESENHANDO ELEMENTOS DOS OBSTÁCULOS
            # 5.1 Desenahndo os Obstáculos
        self.obstaculos.draw(self.surface)

        # 6.0 ===== DESENHANDO ELEMENTOS DOS INIMIGOS
            # 6.1 Desenhando os inimigos
        self.inimigos.draw(self.surface)

        # 7.0 ===== DESENHANDO ELEMENTOS DO PLAYER
            # 7.1 Desenhando o player
        self.player.desenhar(self.surface)

        # 8.0 ===== DESENHANDO ELEMENTOS DO HUD =====
            # 8.1 Desenando o Hud                       #(x, y, width, height)
        pygame.draw.rect(self.surface, CORES["PRETO"], (0, SCREEN_CONFIG["HEIGHT"] - SCREEN_CONFIG["HEIGHT_HUD"],
                                                        SCREEN_CONFIG["WIDTH"], SCREEN_CONFIG["HEIGHT_HUD"]))

            # 8.2 Renderiza o Score no HUD
        renderiza_text(True, self.surface,  FONTES["OPCAO"], 15, f'SCORE', CORES["BRANCO"],
                       SCREEN_CONFIG["CENTER_X"], SCREEN_CONFIG["HEIGHT"] - 50, "MID_TOP") # Renderiza o Nome SCORE na Superfície *

        renderiza_text(True, self.surface,  FONTES["OPCAO"], 15, f'{self.score}',
                       CORES["BRANCO"], SCREEN_CONFIG["CENTER_X"], SCREEN_CONFIG["HEIGHT"] - 30,
                       "MID_TOP") # Renderiza o Score

            # 8.3 Renderiza o Melhor Score no HUD
        renderiza_text(True, self.surface,  FONTES["OPCAO"], 15, "MELHOR SCORE", CORES["BRANCO"],
                       SCREEN_CONFIG["WIDTH"] - 10, SCREEN_CONFIG["HEIGHT"] - 50, "TOP_RIGHT") # O MESMO *

        renderiza_text(True, self.surface,  FONTES["OPCAO"], 15, f"{self.melhor_score}", CORES["BRANCO"],
                       SCREEN_CONFIG["WIDTH"] - 10, SCREEN_CONFIG["HEIGHT"] - 30, "TOP_RIGHT") # O MESMO *

            # 8.4 Renderiza o Velocímetro no HUD
        renderiza_text(True, self.surface,  FONTES["OPCAO"], 15, "VELOCÍMETRO", CORES["BRANCO"],
                       10, SCREEN_CONFIG["HEIGHT"] - 50)  # O MESMO *

        renderiza_text(True, self.surface,  FONTES["OPCAO"], 15, f"{self.vel_display} Km/h", CORES["BRANCO"],
                       10, SCREEN_CONFIG["HEIGHT"] - 30)  # O MESMO *

            # 8.5 Renderizar a IMAGEM da barra de vida no HUD
        self.surface.blit(carregar_imagem(CENARIO["BARRA_VIDA"]), (POS_INICIAIS["BARRA_VIDA_X"],
                                                                   POS_INICIAIS["BARRA_VIDA_Y"]))

            # 8.6 Desenhando a Barra de Vida
        if self.player.largura_barra_vida > HP["FIM"] and self.player.largura_barra_vida <= HP["LARGURA_BARRA_VIDA"]:
            pygame.draw.rect(self.surface, CORES["VERDE"], (HP["BARRA_VIDA_RECT_X"],
                                                            HP["BARRA_VIDA_RECT_Y"], self.player.largura_barra_vida, HP["ALTURA_BARRA_VIDA"]))

        elif self.player.largura_barra_vida < HP["INICIO"] and self.player.largura_barra_vida >= HP["VIDA_MIN_PLAYER"]:
            pygame.draw.rect(self.surface, CORES["VERMELHO"], (HP["BARRA_VIDA_RECT_X"],
                                                               HP["BARRA_VIDA_RECT_Y"], self.player.largura_barra_vida, HP["ALTURA_BARRA_VIDA"]))

        else:
            pygame.draw.rect(self.surface, CORES["AMARELO"], (HP["BARRA_VIDA_RECT_X"],
                                                              HP["BARRA_VIDA_RECT_Y"], self.player.largura_barra_vida, HP["ALTURA_BARRA_VIDA"]))

        screen.blit(self.surface, (0, 0)) # Cria a superfície principal
    # desenhar()
# Fase1:
