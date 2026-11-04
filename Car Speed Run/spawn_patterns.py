PADROES_SPAWN = [
    # ===== PADRÕES SIMPLES (1 objeto) =====
    {
        "nome": "inimigo_unico",
        "peso": 30,
        "objetos": [
            {"tipo": "inimigo", "faixas": [0, 1]},  # sorteia entre faixa 0 e 1
        ],
    },
    {
        "nome": "obstaculo_unico",
        "peso": 20,
        "objetos": [
            {"tipo": "obstaculo", "faixas": [0, 1, 2]},
        ],
    },
    {
        "nome": "oleo_unico",
        "peso": 15,
        "objetos": [
            {"tipo": "oleo", "faixas": [0, 1, 2]},
        ],
    },

    # ===== PADRÕES DUPLOS (2 objetos de tipos diferentes) =====
    {
        "nome": "inimigo_obstaculo",
        "peso": 15,
        "objetos": [
            {"tipo": "inimigo", "faixas": [0, 1]},
            {"tipo": "obstaculo", "faixas": [2]},  # força na faixa 2
        ],
    },
    {
        "nome": "inimigo_oleo",
        "peso": 10,
        "objetos": [
            {"tipo": "inimigo", "faixas": [0, 1]},
            {"tipo": "oleo", "faixas": [2]},
        ],
    },

    # ===== PADRÕES DUPLOS DE INIMIGO (mesmo tipo, faixas diferentes) =====
    {
        "nome": "dois_inimigos",
        "peso": 10,
        "objetos": [
            {"tipo": "inimigo", "faixas": [0]},
            {"tipo": "inimigo", "faixas": [1]},
        ],
    },
]