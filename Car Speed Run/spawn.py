# ===== IMPORTAÇÕES =====
from Objetos.inimigos import Inimigos
from Objetos.obstaculos import Obstaculos
from Objetos.oleo import Oleo

from spawn_patterns import PADROES_SPAWN

from random import choices, choice


def sortear_padrao():
    # Pesos (relativos)
    pesos = [p["peso"] for p in PADROES_SPAWN]

    # Sorteia um padrão com base nos pesos
    padrao = choices(PADROES_SPAWN, weights=pesos, k=1)[0]
    return padrao
# sortear_padrao()


def criar_objetos_do_padrao(padrao, grupos):
    """
    grupos = {
        "inimigo": grupo_inimigos,
        "obstaculo": grupo_obstaculos,
        "oleo": grupo_oleo,
    }
    """
    for obj_spec in padrao["objetos"]:
        tipo = obj_spec["tipo"]
        faixas = obj_spec["faixas"]
        faixa_sorteada = choice(faixas)

        if tipo == "inimigo":
            grupos["inimigo"].add(Inimigos(faixa=faixa_sorteada))
        elif tipo == "obstaculo":
            grupos["obstaculo"].add(Obstaculos(faixa=faixa_sorteada))
        elif tipo == "oleo":
            grupos["oleo"].add(Oleo(faixa=faixa_sorteada))
        # ... penhasco com cooldown ...
# criar_objetos_do_padrao()
