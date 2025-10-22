# main.py
"""
Script principal para executar a análise de custos logísticos
"""

import sys
import os

def configurar_ambiente():
    """Configura o ambiente e paths corretamente"""
    
    # Obtém o diretório do script atual
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(current_dir, 'src')
    
    print(f"📁 Diretório do script: {current_dir}")
    print(f"📁 Caminho src: {src_path}")
    
    # Verifica se a pasta src existe
    if not os.path.exists(src_path):
        print("❌ ERRO: Pasta 'src' não encontrada!")
        print("📁 Criando estrutura de pastas...")
        os.makedirs(src_path, exist_ok=True)
        return False
    
    # Adiciona src ao path do Python
    if src_path not in sys.path:
        sys.path.insert(0, src_path)
        print(f"✅ Pasta src adicionada ao Python path")
    
    # Verifica se os módulos existem
    modulos_necessarios = ['data_loader.py', 'visualizacoes.py', 'modelos.py']
    for modulo in modulos_necessarios:
        modulo_path = os.path.join(src_path, modulo)
        if not os.path.exists(modulo_path):
            print(f"❌ ERRO: {modulo} não encontrado em {src_path}")
            return False
    
    print("✅ Ambiente configurado com sucesso!")
    return True

def importar_modulos():
    """Importa os módulos com tratamento de erro"""
    try:
        from data_loader import carregar_dados_diarios, carregar_dados_mensais, carregar_acoes, calcular_kpis
        from visualizacoes import plot_evolucao_mensal, plot_composicao_custos, plot_correlacao, plot_distribuicao_custo_km
        from modelos import ModeladorCustos
        import matplotlib.pyplot as plt
        
        print("✅ Módulos importados com sucesso!")
        return (carregar_dados_diarios, carregar_dados_mensais, carregar_acoes, calcular_kpis,
                plot_evolucao_mensal, plot_composicao_custos, plot_correlacao, plot_distribuicao_custo_km,
                ModeladorCustos, plt)
        
    except ImportError as e:
        print(f"❌ ERRO na importação: {e}")
        print("📝 Verifique se os arquivos estão na pasta src/")
        return None

def analise_completa():
    """Executa análise completa dos dados"""
    
    print("🚀 INICIANDO ANÁLISE DE CUSTOS LOGÍSTICOS")
    print("=" * 50)
    
    # Configura ambiente
    if not configurar_ambiente():
        return
    
    # Importa módulos
    modulos = importar_modulos()
    if modulos is None:
        return
        
    (carregar_dados_diarios, carregar_dados_mensais, carregar_acoes, calcular_kpis,
     plot_evolucao_mensal, plot_composicao_custos, plot_correlacao, plot_distribuicao_custo_km,
     ModeladorCustos, plt) = modulos
    
    # 1. Carregar dados
    print("\n📊 CARREGANDO DADOS...")
