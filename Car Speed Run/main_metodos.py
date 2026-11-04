'''
    Aqui estarão todos os principais métodos do jogo como rendirizar textos,
    criar superfícies e mais. Geralmente os médotos que serão usados mais de
    uma vez!
'''
# =====BIBLIOTECAS IMPORTADAS =====
import pygame
from main_config import SCREEN_CONFIG, CORES, ALINHAMENTOS


# =============== MÉTODO  PARA RENDERIZAR TEXTO ===============
def renderiza_text(modelo, screen, font_type, font_size, msg, msg_color, msg_posx, msg_posy, alinhamento="TOP_LEFT"):
    """
    --> Função para renderizar textos na tela
    :param modelo: Uma booleana que determina a fonte que será usada: False - escolha do sistema; True - Use uma Baixada
    :param screen: Determina a superfície onde o texte será renderizado
    :param font_type: Nome da fonte escolhida
    :param font_size: Tamanho da fonte escolhida
    :param msg: Nome do texto renderizado
    :param msg_color: Cor do texto renderizado
    :param msg_posx: Posição horizontal (x) do texto renderizado
    :param msg_posy: Posição vertical (y) do texto renderizado
    :param centralizado: Booleana - True para tornar msg_posx e msg_posy como coordenada cental: rect.center (msg_posx, msg_posy)
    :return:NONE
    """

    if not modelo:
        font = pygame.font.SysFont(font_type, font_size)
    else:
        font = pygame.font.Font(font_type, font_size)

    text = font.render(msg, True, msg_color)
    rect = text.get_rect()

    setattr(rect, ALINHAMENTOS[alinhamento], (msg_posx, msg_posy))
    screen.blit(text, rect)
# renderiza_text()


def desenha_opcoes_Menu(modo, surface, lista, fonte, cor_opc_select, cor_not_select, num_index_select):
    # Criando a Lista de opções do Menu
    opcoes = lista
    cor_selecionada = CORES.get(cor_opc_select, CORES["BRANCO"]) # garante que o texto será renderisado caso aja erro de grafia da chave *
    cor_normal = CORES.get(cor_not_select, CORES["BRANCO"]) # O MESMO *

    for i, opc in enumerate(opcoes):
        cor = cor_selecionada if i == num_index_select else cor_normal
        renderiza_text(modo, surface, fonte, 40, opc, cor, SCREEN_CONFIG["CENTER_X"],
                       SCREEN_CONFIG["CENTER_Y"] + i * 60, "CENTER")
# desenha_opcoes_Menu()

