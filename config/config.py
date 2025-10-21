
## 11. config/config.py


"""
Configurações globais do projeto
"""

# Configurações de análise
RANDOM_STATE = 42
TEST_SIZE = 0.2
N_ESTIMATORS = 100

# Cores para visualizações
CORES = {
    'primaria': '#1f77b4',
    'secundaria': '#ff7f0e',
    'terciaria': '#2ca02c',
    'destaque': '#d62728',
    'neutra': '#7f7f7f'
}

# KPIs metas
METAS = {
    'custo_km_max': 0.22,
    'margem_minima': 15.0,
    'dias_negativos_mes': 0,
    'variabilidade_combustivel': 20.0
}

# Configurações de visualização
CONFIG_VISUALIZACAO = {
    'figsize': (12, 6),
    'dpi': 100,
    'style': 'default'
}
