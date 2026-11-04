'''
Aqui é o código principal do jogo onde o loop central irá rodar, onde erros e bugs serão
verificados impedindo que aja uma travamento generalizado do código
'''

# ===== IMPORTAÇÕES PRINCIPAIS =====
from setup import inicializa_pygame

# ===== IMPORTÇÕES DE MÉTODOS E CONFIGURÇÕES =====
from main_config import GAMESTATE


# ===== IMPORTAÇÕES DE CLASSES =====
import Fases.gerenciador_fases as GF
from Fases.fase_Menu import FaseMenu
from Fases.primeira_fase import Fase1
from Fases.fase_game_over import GameOver


'''def main():
    print('Iniciando o Game') # mensagem de inicialização do jogo

    try:
        # 1. INICIALIZAÇÃO DO PYGAME
        pygame.init()

        # 1.1 INICIALIZAÇÃO DO MIXER
        pygame.mixer.init()

        # 2. CONFIGURAÇÕES BÁSICAS

        # 2.1 DIMENSIONANDO E NOMEANDO A TELA
        screen = pygame.display.set_mode((SCREEN_CONFIG['WIDTH'], SCREEN_CONFIG['HEIGHT']))
        pygame.display.set_caption(SCREEN_CONFIG['GAME NAME'])

        #pygame.mouse.set_visible(0) # Deixa o cursor do mouse invisível

        # 3. RELÓGIO PARA CONTROLAR O FPS
        clock = pygame.time.Clock()

        # 4. VARIÁVEL DE CONTROLE DO LOOP PRINCIPAL
        running = True
        print('Jogo pronto para executar')

        # 5. LOOP PRINCIPAL DO JOGO
        while running:

            # ===== PROCESSAMENTO DE EVENTOS =====
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    print('saindo do Jogo...')

                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        print('O ESC precionado, saindo...')

            # ===== ATUALIZAÇÃO DA LÓGICADO JOGO =====
            # Controlando os Estados do Jogo

            # ===== RENDERIZAÇÃO (DESENHANDO NA TELA) =====
            # 1. Limpa a tela com a cor preta
            screen.fill(CORES["BACKGROUND COLOR"]) # remove frames anteriores

            # 2.Desenhando elementos do Jogo (Background)

            # 2.1 Desenhando o Título da Tela do Menu
            renderiza_text(True, screen, 'Fonts/Silkscreen-Regular.ttf', 50, 'MENU', CORES['BRANCO'], SCREEN_CONFIG["CENTER_X"], 10, "MID_TOP")
            desenha_opcoes_Menu(screen, ["START", "OPÇÕES"], 'Fonts/NovaSquare-Regular.ttf')

            # 2.2 Criando, Desenhando e Atualizando o Botão START

            # 3. Atualizando a tela
            pygame.display.flip()

            # ===== CONTROLE DE VELOCIDADE DO JOGO =====
            clock.tick(SCREEN_CONFIG['FPS'])

    except Exception as e:
        # CAPTURA DE ERROS
        print(f'ERRO crítico {e}')
        import traceback
        traceback.print_exc()

    finally: # garante que o comando "quit()" sempre será executado
        # LIMPEZA FINAL
        print('Limpando recursos')
        quit()
        sys.exit()
# main()'''

# PONTO DE ENTREGA DO PROGAMA
if __name__ == '__main__':
    # Cria o gerenciador

    screen, clock = inicializa_pygame()

    gerenciador = GF.GerenciadorFases(screen, clock)

    # Cria e adiciona as fases
    gerenciador.adicionar_fase(GAMESTATE["MENU"], FaseMenu())
    gerenciador.adicionar_fase(GAMESTATE["FASE1"], Fase1())
    gerenciador.adicionar_fase(GAMESTATE["GAMEOVER"], GameOver())

    # Inicia com o menu
    gerenciador.mudar_fase(GAMESTATE["MENU"])

    # Executa o jogo
    gerenciador.loop()

