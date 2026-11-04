"""
    O Objetivo deste módulo é garantir que as imagens sejam sempre carregadas e carreghuem
    apenas uma única vez, para liberar espaço de memória
"""

# ===== IMPORTAÇÕES =====
import pygame

# ===== CACHES =====
_cache_imagens = {}
_cache_sons = {}

# ===== método para realizar o carregamento das imagens =====
def carregar_imagem(caminho):
    ''' carrega uma imagem do disco ou do cache'''
    if caminho not in _cache_imagens: # verifica se a imagem a ser carregada esta no cache
        _cache_imagens[caminho] = pygame.image.load(caminho).convert_alpha()
    return _cache_imagens[caminho]

# ===== método para realizar o carregamento dos sons =====

def carregar_sons(caminho):
    ''' carrega um som do disco ou do cache'''
    if caminho not in _cache_sons:
        _cache_sons[caminho] = pygame.mixer.Sound(caminho)
    return _cache_sons[caminho]

# ===== método para realizar o carregamento das músicas =====
def carregar_musicas(caminho):
    '''carrega uma música (não um cache - music é canal único)'''
    pygame.mixer.music.load(caminho)

# ===== método para realizar a limpesa dos caches =====
def limpar_caches():
    '''limpa os caches - (útil para o debug)'''
    _cache_imagens.clear()
    _cache_sons.clear()
