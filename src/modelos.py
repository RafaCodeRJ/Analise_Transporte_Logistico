"""
Módulo para modelagem preditiva
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

class ModeladorCustos:
    """Classe para modelagem preditiva de custos logísticos"""
    
    def __init__(self, random_state=42):
        self.random_state = random_state
        self.modelos = {}
        self.resultados = {}
        
    def preparar_dados(self, df: pd.DataFrame, test_size=0.2):
        """Prepara dados para modelagem"""
        features = ['KM Percorridos', 'Entregas', 'Peso (ton)', 'Frete', 'Margem', 
                   'Custo Combustível', 'Custo Manutenção', 'Custo Motorista']
        target = 'Custo Total'
        
        X = df[features]
        y = df[target]
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_state
        )
        
        print(f"✅ Dados preparados: {len(self.X_train)} treino, {len(self.X_test)} teste")
        
    def treinar_regressao_linear(self):
        """Treina modelo de regressão linear"""
        modelo = LinearRegression()
        modelo.fit(self.X_train, self.y_train)
        
        # Previsões
        y_pred = modelo.predict(self.X_test)
        
        # Métricas
        mse = mean_squared_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)
        
        self.modelos['Regressão Linear'] = modelo
        self.resultados['Regressão Linear'] = {
            'mse': mse,
            'r2': r2,
            'y_pred': y_pred
        }
        
        print(f"✅ Regressão Linear - MSE: {mse:.2f}, R²: {r2:.4f}")
        
    def treinar_random_forest(self, n_estimators=100):
        """Treina modelo Random Forest"""
        modelo = RandomForestRegressor(
            n_estimators=n_estimators,
            random_state=self.random_state
        )
        modelo.fit(self.X_train, self.y_train)
        
        # Previsões
        y_pred = modelo.predict(self.X_test)
        
        # Métricas
        mse = mean_squared_error(self.y_test, y_pred)
        r2 = r2_score(self.y_test, y_pred)
        
        self.modelos['Random Forest'] = modelo
        self.resultados['Random Forest'] = {
            'mse': mse,
            'r2': r2,
            'y_pred': y_pred,
            'importancias': modelo.feature_importances_
        }
        
        print(f"✅ Random Forest - MSE: {mse:.2f}, R²: {r2:.4f}")
        
    def comparar_modelos(self):
        """Compara performance dos modelos"""
        comparacao = []
        for nome, resultados in self.resultados.items():
            comparacao.append({
                'Modelo': nome,
                'MSE': resultados['mse'],
                'R²': resultados['r2']
            })
        
        df_comparacao = pd.DataFrame(comparacao)
        return df_comparacao.sort_values('R²', ascending=False)
    
    def plot_importancia_features(self):
        """Plota importância das features no Random Forest"""
        if 'Random Forest' not in self.modelos:
            print("❌ Modelo Random Forest não treinado")
            return
        
        importancias = self.resultados['Random Forest']['importancias']
        features = self.X_train.columns
        
        indices = np.argsort(importancias)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=importancias[indices], y=features[indices], palette='viridis')
        ax.set_title('Importância das Variáveis - Random Forest', fontweight='bold')
        ax.set_xlabel('Importância Relativa')
        plt.tight_layout()
        
        return fig
    
    def plot_previsoes_vs_reais(self):
        """Plota comparação entre valores reais e previstos"""
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        for idx, (nome, resultados) in enumerate(self.resultados.items()):
            ax = axes[idx]
            y_pred = resultados['y_pred']
            
            ax.scatter(self.y_test, y_pred, alpha=0.6)
            ax.plot([self.y_test.min(), self.y_test.max()], 
                    [self.y_test.min(), self.y_test.max()], 'r--', lw=2)
            ax.set_title(f'{nome}\nR² = {resultados["r2"]:.4f}')
            ax.set_xlabel('Valor Real')
            ax.set_ylabel('Valor Previsto')
            ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        return fig
