"""
    Neste Módula será criado um arquivo txt para salvar a melhor pontuação do jogo
"""
# ===== IMPORTAÇÕES =====
import os

ARQUIVO = 'melhor_score.txt'


def carregar():
    """ Lê o melhor score do arquivo. Caso não exista retorna 0"""
    if os.path.exists(ARQUIVO): # Verifica se existe conteúdo na variável ARQUIVO
        with open(ARQUIVO, "r") as f: # Caso aja abre o arquivo para leitura
            conteudo = f.read().strip() # retirando os espaços do conteúdo do arquivo
            return int(conteudo) if conteudo else 0 # caso o aquivo esteja vazio me mostro o valor numérico 0
    return 0
# carregar()

def salvar(valor):
    """ Salva o melhor score no arquivo"""
    with open(ARQUIVO, "w") as f: # abra o arquivo no modo edição "w"
        f.write(str(valor)) # salve o valor no arquivo como um texto
# salvar()
