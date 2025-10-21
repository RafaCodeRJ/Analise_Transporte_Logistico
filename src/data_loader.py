"""
Módulo para carregamento e preparação dos dados logísticos
"""

import pandas as pd
import numpy as np
from typing import Tuple, Dict

def carregar_dados_diarios(caminho: str = '../data/dados_logistica.csv') -> pd.DataFrame:
    """
    Carrega e prepara os dados diários de logística
    
    Parametros:
    caminho (str): Caminho para o arquivo CSV
    
    Retornos:
    pd.DataFrame: DataFrame com dados preparados
    """
    try:
        df = pd.read_csv(caminho, parse_dates=['Data'])
        print(f"✅ Dados diários carregados: {len(df)} registros")
        return df
    except FileNotFoundError:
        print("❌ Arquivo não encontrado. Verifique o caminho.")
        return pd.DataFrame()

def carregar_dados_mensais(caminho: str = '../data/dados_mensais.csv') -> pd.DataFrame:
    """
    Carrega os dados mensais consolidados
    """
    try:
        df = pd.read_csv(caminho)
        print(f"✅ Dados mensais carregados: {len(df)} meses")
        return df
    except FileNotFoundError:
        print("❌ Arquivo mensal não encontrado.")
        return pd.DataFrame()

def carregar_acoes(caminho: str = '../data/tabela_acoes.csv') -> pd.DataFrame:
    """
    Carrega a tabela de ações prioritárias
    """
    try:
        df = pd.read_csv(caminho)
        print(f"✅ Ações carregadas: {len(df)} ações")
        return df
    except FileNotFoundError:
        print("❌ Arquivo de ações não encontrado.")
        return pd.DataFrame()

def calcular_kpis(df_diario: pd.DataFrame) -> Dict:
    """
    Calcula KPIs principais dos dados diários
    
    Returns:
    Dict: Dicionário com KPIs calculados
    """
    kpis = {
        'custo_medio_km': df_diario['Custo/KM'].mean(),
        'entregas_media_dia': df_diario['Entregas'].mean(),
        'margem_media': df_diario['Margem %'].mean(),
        'custo_total_medio': df_diario['Custo Total'].mean(),
        'frete_medio': df_diario['Frete'].mean(),
        'km_medio_dia': df_diario['KM Percorridos'].mean()
    }
    return kpis

def preparar_dados_modelagem(df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
    """
    Prepara dados para modelagem preditiva
    
    Returns:
    Tuple: Features (X) e target (y)
    """
    features = ['KM Percorridos', 'Entregas', 'Peso (ton)', 'Frete', 'Margem', 
               'Custo Combustível', 'Custo Manutenção', 'Custo Motorista']
    target = 'Custo Total'
    
    X = df[features]
    y = df[target]
    
    return X, y
