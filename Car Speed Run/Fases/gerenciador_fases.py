# ===== IMPORTAÇÕES =====
import pygame
import sys
from main_config import SCREEN_CONFIG


class GerenciadorFases:
    """Gerencia as fases do jogo"""

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.fases = {}
        self.fase_atual = None
        self.rodando = True

    def adicionar_fase(self, nome, fase):
        """Adiciona uma fase ao gerenciador"""
        self.fases[nome] = fase

    def mudar_fase(self, nome):
        """Troca para uma fase específica"""
        # Finaliza a fase atual
        if self.fase_atual:
            self.fases[self.fase_atual].finalizar()

        # Inicia a nova fase
        if nome in self.fases:
            self.fase_atual = nome
            self.fases[nome].iniciar()
            print(f"📱 Mudou para fase: {nome}")
        else:
            print(f"❌ Fase '{nome}' não encontrada!")

    def loop(self):
        """Loop principal do jogo"""
        while self.rodando:
            # Executa o loop da fase atual
            if self.fase_atual:
                fase = self.fases[self.fase_atual]

                # SE a fase retornar False, encerra o jogo
                if not fase.loop(self.screen):
                    self.rodando = False  # ← Encerra o loop principal

                # ✅ checa se a fase pediu troca
                if getattr(fase, "proxima_fase", None):
                    destino = fase.proxima_fase
                    fase.proxima_fase = None
                    self.mudar_fase(destino)

            else:
                print("⚠️ Nenhuma fase selecionada!")
                break

            self.clock.tick(SCREEN_CONFIG["FPS"])

        pygame.quit()
        sys.exit()
