"""
    Neste móduto terá a classe construtora de todas as fazes que possa existir no Jogo
"""
# ===== IMPORTAÇÕES =====
import pygame
from pygame.locals import *
from main_config import SCREEN_CONFIG


class Fase:
    """Classe base para criar fases independentes"""

    def __init__(self, cor_fundo, nome):
        # Cria a superfície da fase com as dimensões da tela
        self.surface = pygame.Surface((SCREEN_CONFIG["WIDTH"], SCREEN_CONFIG["HEIGHT"]))
        self.cor_fundo = cor_fundo
        self.nome = nome
        self.ativo = False  # Controla se a fase está rodando
        self.proxima_fase = None

    def iniciar(self):
        """Ativa a fase e prepara ela para rodar"""
        self.ativo = True
        print(f"🟢 Iniciando fase: {self.nome}")

    def finalizar(self):
        """Desativa a fase e limpa recursos"""
        self.ativo = False
        print(f"🔴 Finalizando fase: {self.nome}")

    def processar_eventos(self, eventos):
        """Processa os eventos da fase - deve ser sobrescrito"""
        """
           Processa os eventos da fase.
           Retorna True se a fase deve continuar, False se deve encerrar o jogo.
        """
        # 1. Processa eventos
        for event in eventos:
            if event.type == QUIT:
                return False  # Sinaliza que o jogo deve fechar
        return True  # Fase continua normalmente

    def atualizar(self):
        """Atualiza a lógica da fase - deve ser sobrescrito"""
        pass

    def desenhar(self, screen):
        """Desenha a fase na tela - deve ser sobrescrito"""
        # Preenche a superfície com a cor de fundo
        self.surface.fill(self.cor_fundo)

        # Desenha a superfície na tela
        screen.blit(self.surface, (0, 0))

    def loop(self, screen):
        """Loop completo da fase - executa um frame"""
        if not self.ativo:
            return

        # 1. Processa eventos
        eventos = pygame.event.get()

        # SE processar_eventos retornar False, encerra o jogo
        if not self.processar_eventos(eventos):
            return False

        # 2. Atualiza lógica
        self.atualizar()

        # 3. Desenha na tela
        self.desenhar(screen)

        # 4. Atualiza a tela
        pygame.display.flip()

        return True  # Fase continua normalmente
