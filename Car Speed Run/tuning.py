"""
    Neste módulo estão contidicionários para todas as variáveis de contro do jogo, como os valores de velocidade
    do player, inimigos etc. A taxa de spaw entre outros.
"""
# ===== IMPORTAÇÕES =====


# ========== REUNE TODAS AS VELOCIDADES QUE O JOGO UTILIZA ==========
VELOCIDADES = {
    "VELOCIDADE_SCROLL":            4,
    "AUMENTO_VEL_SCROLL":           0.04,
    "VELOCIDADE_MAX_SCROLL":        20,
    "VELOCIDADE_X_PLAYER":          4,
    "AUMENTO_VEL_X_PLAYER":         0.004,
    "VELOCIDADE_X_MAX_PLAYER":      10,
    "VELOCIDADE_Y_INIMIGOS":        10,
    "AUMENTO_VEL_Y_INIMIGOS":       0.08,
    "VELOCIDADE_Y_MAX_INIMIGOS":    40,
    "VELOCIDADE_PULO":              3,

}

# ========== REUNE TODOS OS INTERVALOS DE SPAW QUE O JOGO UTILIZA ==========
SPAWNS ={
    "INTERVALO_SPAW_GERAL":         60,
    "COOLDOWN_SPAWN_PENHASCO":      0,
    "DURACAO_COOLDOWN":             2 * 60,
    "INTERVALO_PENHASCO":           10 * 60,
}

# ========== REUNE TODOS OS CONTADORES QUE O JOGO UTILIZA ==========
CONTADORES = {
    "TIMER_SPAW_GERAL":             0,
    "INCREMENTO_TIMER_SPAW_GERAL":  1,
    "INCREMENTO_TIMER_GIRO":        1,
    "INCREMENTO_ANGULO_GIRO":       15,
    "INCREMENTO_DESLOC_X_PLAYER":   3,
    "INCREMENTO_DESLOC_Y_PLAYER":   2,
    "SCORE":                        0,
    "TEMPO_ESPERA_MENU":            0,
    "DURACAO_ESPERA_MENU":          120,
    "INCREMENTO_TEMPO_ESPERA_MENU": 1,
    "TIMER_COR":                    0,
    "DURACAO_COR_ON":               30,
    "DURACAO_COR_OFF":              30,
    "INCREMENTO_COR":               1,
    "TIMER_PENHASCO":               0,
    "DECRESCIMO_COOLDOWN":          1,
    "INCREMENTO_SPAWN_PENHASCO":    1,

}

# ========== REUNE TODOS OS MULTIPLICADORES QUE O JOGO UTILIZA ==========
MULTIPLICADORES = {
    "MULT_SCORE":                   10,
    "MULT_VELOCIMETRO":             300,
    "MULT_ANGULO":                  360,
}

# ========== REUNE TODOS AS VARIÁVEIS DE CONTROLO QUE O JOGO UTILIZA ==========
VARIAVEIS_DE_CONTROLE = {
    "LARGURA_FAIXA":                100,
    "ESPACO_ENTRE_FAIXAS":          75,
    "ANGULO_GIRO_PLAYER":           0,
    "TIMER_GIRO_PLAYER":            0,
    "DURACAO_GIRO_PLAYER":          60,
    "LIMITE_DIREITO_PISTA":         280,
    "LIMITE_ESQUEDO_PISTA":         70,
    "LIMITE_QUEDA_PISTA":           350,
    "AJUSTE_POS_CHEGADA":           100,
    "QTDE_GELO_BAIANO_CRIADO":      12,
    "ESPACO_ENTRE_GELO_BAIANO":     50,
    "ALTURA_MAX_PULO":              100,
    "ALTURA_INICIAL":               0,
    "QTDE_ACOSTAMENTO":             11,
    "ESPACO_ENTRE_ACOSTAMENTO":     50,
    "QTDE_PISTA":                   2,
}

# ========== REUNE TODOS AS POSIÇÕES INICIAIS QUE O JOGO UTILIZA ==========
_DIMENSAO = 500 # REPRESENTA A DIMENSÃO VERTICAL DA PISTA
POS_INICIAIS = {
    "PISTA_1_X":                50,
    "PISTA_1_Y":                0,
    "PISTA_2_X":                50,
    "PISTA_2_Y":                - _DIMENSAO,
    "CHEGADA_X":                50,
    "CHEGADA_Y":                - _DIMENSAO * 2, # Caso o comprimento da pista mude mudar valor manualmente aqui
    "OLEO_Y":                   600 / 4,
    "BARRA_VIDA_X":             0,
    "BARRA_VIDA_Y":             500,
    "ACOSTAMENTO_ESQUEDO":      0,
    "ACOSTAMENTO_DIREITO":      350
}

# ========== REUNE TODOS AS POSIÇÕES INICIAIS QUE O JOGO UTILIZA ==========
LIMITADORES = {
    "SCORE_MAX": 9999999,
}

_LARGURA = 336 # REPRESENTA A LARGURA DA BARRA DE VIDA
HP = {
    "TAXA_GANHO_VIDA":      0.5,
    "TAXA_PERDA_VIDA":      2,
    "VIDA_MAX_PLAYER":      100,
    "VIDA_MIN_PLAYER":      0,
    "VIDA_PLAYER":          100,
    "LARGURA_BARRA_VIDA":   _LARGURA,
    "ALTURA_BARRA_VIDA":    18,
    "BARRA_VIDA_RECT_X":    54,
    "BARRA_VIDA_RECT_Y":    516,
    "FIM":                  (2 * _LARGURA) / 3,
    "INICIO":               _LARGURA / 3
}
# ===== FIM