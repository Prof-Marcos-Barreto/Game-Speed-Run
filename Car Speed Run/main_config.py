'''
Aquie terão todas as principais variaveis para serem acessadas quando necessário!!
Limpando e organizando o código e facilitando alterações futuras, quando necessário
'''
from tuning import VARIAVEIS_DE_CONTROLE, _DIMENSAO
# ==================== MODIFICAÇÕES PARA TELA ====================

# ===== CONFIGURAÇÕES DE TELA =====
SCREEN_CONFIG = {
    'WIDTH': 400,
    'HEIGHT': 600,
    'HEIGHT_HUD': 100,
    'HEIGHT_PISTA': 500,
    'CENTER_X': (400 / 2),
    'CENTER_Y': (600 / 2),
    'GAME_NAME': 'Car Speed Run',
    'FPS': 60
}

# ===== CORES (RGB) =====
CORES = {
    'PRETO':                (0, 0, 0),
    'BRANCO':               (255, 255, 255),
    'VERMELHO':             (255, 0, 0),
    'VERDE':                (0, 255, 0),
    'AZUL':                 (0, 0, 255),
    'AMARELO':              (255, 255, 0),
    'SHADOW BUTTON COLOR':  (0, 48, 143),
    'BACKGROUND COLOR':     (10, 10, 10, 0.5)
}

# ===== ALINHAMENTO DE TEXTOS =====
ALINHAMENTOS = {
    "TOP_LEFT":      "topleft",
    "TOP_RIGHT":     "topright",
    "BOTTOM_LEFT":   "bottomleft",
    "BOTTOM_RIGHT":  "bottomright",
    "MID_TOP":       "midtop",
    "MID_BOTTOM":    "midbottom",
    "MID_LEFT":      "midleft",
    "MID_RIGHT":     "midright",
    "CENTER":        "center",
    "CENTER_X":      "centerx",
    "CENTER_Y":      "centery",
}

# ===== FONTES DE TEXTO =====
FONTES ={
    "TITULO": "Fonts/Silkscreen-Regular.ttf",
    "OPCAO": 'Fonts/NovaSquare-Regular.ttf'
}

# ==================== MODIFICAÇÕES DOS PERSONAGENS ====================
# ===== DIMENSÕES DOS PERSONAGENS =====
DIM_OBJETOS ={
    "DIM_PLAYER": {
        "WIDTH": 50, "HEIGHT": 150
    },
    "DIM_INIMIGOS": {
        "WIDTH": 50, "HEIGHT": 150
    },
    "DIM_OBSTACULOS": {
        "WIDTH": 100, "HEIGHT": 100
    },
    "DIM_OLEO": {
        "WIDTH": 100, "HEIGHT": 100
    },
    "DIM_PENHASCO": {
        "WIDTH": 400, "HEIGHT": 450
    },
    "DIM_GELO-BAIANO": {
        "WIDTH": 20, "HEIGHT": 40
    },
    "DIM_ACOSTAMENTO": {
        "WIDTH": 50, "HEIGHT": 50
    },
    "DIM_PISTA": {
        "WIDTH": SCREEN_CONFIG["WIDTH"] - SCREEN_CONFIG["HEIGHT_HUD"],
        "HEIGHT": SCREEN_CONFIG["HEIGHT_PISTA"]
    }
}

# ===== POSIÇÕES DOS PERSONAGENS =====
POS_OBJETOS = {
    "POS_PLAYER": {
        "X": SCREEN_CONFIG["CENTER_X"] - DIM_OBJETOS["DIM_PLAYER"]["WIDTH"] * 2,
        "Y": SCREEN_CONFIG["HEIGHT_PISTA"] - DIM_OBJETOS["DIM_PLAYER"]["HEIGHT"]
    },
    "POS_INIMIGOS": {
        "X": [SCREEN_CONFIG["CENTER_X"] - DIM_OBJETOS["DIM_INIMIGOS"]["WIDTH"] * 2,
              SCREEN_CONFIG["CENTER_X"] + DIM_OBJETOS["DIM_INIMIGOS"]["WIDTH"]
              ],
        "Y": - SCREEN_CONFIG["HEIGHT"]
    },
    "POS_OBSTACULOS": {
        "X": [(VARIAVEIS_DE_CONTROLE["LARGURA_FAIXA"] -25) + (VARIAVEIS_DE_CONTROLE["ESPACO_ENTRE_FAIXAS"] * 0),
              (VARIAVEIS_DE_CONTROLE["LARGURA_FAIXA"] -25) + (VARIAVEIS_DE_CONTROLE["ESPACO_ENTRE_FAIXAS"] * 1),
              (VARIAVEIS_DE_CONTROLE["LARGURA_FAIXA"] -25) + (VARIAVEIS_DE_CONTROLE["ESPACO_ENTRE_FAIXAS"] * 2)
              ],
        "Y": - SCREEN_CONFIG["HEIGHT"] / 2
    },
    "POS_OLEO": {
        "X": [(VARIAVEIS_DE_CONTROLE["LARGURA_FAIXA"] - 25) + (VARIAVEIS_DE_CONTROLE["ESPACO_ENTRE_FAIXAS"] * 0),
              (VARIAVEIS_DE_CONTROLE["LARGURA_FAIXA"] - 25) + (VARIAVEIS_DE_CONTROLE["ESPACO_ENTRE_FAIXAS"] * 1),
              (VARIAVEIS_DE_CONTROLE["LARGURA_FAIXA"] - 25) + (VARIAVEIS_DE_CONTROLE["ESPACO_ENTRE_FAIXAS"] * 2)
              ],
        "Y": - SCREEN_CONFIG["HEIGHT"] / 4
    },
    "POS_PENHASCO": {
        "X": 0,
        "Y": 0 - DIM_OBJETOS["DIM_PENHASCO"]["HEIGHT"]
    },
    "POS_GELO-BAIANO": {
        "X": SCREEN_CONFIG["CENTER_X"] - 10,
        "Y": - 40
    },
    "POS_ACOSTAMENTO": {
        "X_DIREITO": 350, "X_ESQUERDO": 0,
        "Y": - 50
    },
    "POS_PISTA": {
        "X": 50,
        "Y": - SCREEN_CONFIG["HEIGHT_PISTA"]
    }
}

# ==================== ESTADOS DO JOGO ====================
# ===== ESTADOS DO JOGO =====
GAMESTATE = {"MENU":        "MENU",
             "OPCAO":       "OPÇÃO",
             "INSTRUCAO":   "INSTRUÇÃO",
             "FASE1":       "FASE 1",
             "GAMEOVER":    "GAME OVER",
             "PAUSE":       "PAUSE",
}
# FIM =====