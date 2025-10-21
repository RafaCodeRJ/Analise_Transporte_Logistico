"""
Módulo para visualizações e gráficos da análise logística
"""

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
from typing import List

def configurar_estilo():
    """Configura o estilo padrão dos gráficos"""
    plt.style.use('default')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 12

def plot_evolucao_mensal(df_mensal: pd.DataFrame):
    """Plota evolução mensal de custos, frete e margem"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    ax.plot(df_mensal['Mês'], df_mensal['Custo Total'], marker='o', linewidth=2, label='Custo Total')
    ax.plot(df_mensal['Mês'], df_mensal['Frete'], marker='s', linewidth=2, label='Frete')
    ax.plot(df_mensal['Mês'], df_mensal['Margem'], marker='^', linewidth=2, label='Margem')
    
    ax.set_title('Evolução Mensal de Custos, Frete e Margem', fontsize=16, fontweight='bold')
    ax.set_xlabel('Mês')
    ax.set_ylabel('Valor (R$)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    return fig

def plot_composicao_custos(df_mensal: pd.DataFrame):
    """Plota composição percentual dos custos"""
    custos_medios = df_mensal[['Custo Combustível', 'Custo Manutenção', 'Custo Motorista']].mean()
    labels = ['Combustível', 'Manutenção', 'Motorista']
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfico de pizza
    ax1.pie(custos_medios, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.set_title('Composição Média dos Custos Operacionais')
    
    # Gráfico de barras
    sns.barplot(x=custos_medios.values, y=labels, ax=ax2)
    ax2.set_title('Valor Absoluto dos Custos Médios')
    ax2.set_xlabel('Custo Médio (R$)')
    
    plt.tight_layout()
    return fig

def plot_correlacao(df: pd.DataFrame, variaveis: List[str]):
    """Plota mapa de correlação entre variáveis"""
    corr_matrix = df[variaveis].corr()
    
    fig, ax = plt.subplots(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
                square=True, ax=ax)
    ax.set_title('Mapa de Correlação - Variáveis Operacionais', 
                fontsize=16, fontweight='bold')
    
    return fig

def plot_distribuicao_custo_km(df: pd.DataFrame):
    """Plota distribuição do custo por KM"""
    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.hist(df['Custo/KM'], bins=30, alpha=0.7, edgecolor='black', 
            color='skyblue')
    ax.axvline(df['Custo/KM'].mean(), color='red', linestyle='--', 
              linewidth=2, label=f'Média: R$ {df["Custo/KM"].mean():.3f}/km')
    
    ax.set_xlabel('Custo por KM (R$)')
    ax.set_ylabel('Frequência')
    ax.set_title('Distribuição do Custo por Quilômetro', fontweight='bold')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    return fig
