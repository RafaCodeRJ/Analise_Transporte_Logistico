# 📋 Metodologia da Análise

## 🎯 Objetivo Principal
Desenvolver uma análise completa dos custos logísticos para identificar oportunidades de otimização e criar um plano de ações baseado em dados.

## 📊 Fases da Análise

### 1. Análise Exploratória (EDA)
**Objetivo**: Compreender a estrutura, qualidade e relações nos dados

**Técnicas utilizadas**:
- Estatística descritiva (média, mediana, desvio padrão)
- Análise de distribuições e outliers
- Matriz de correlação
- Visualizações temporais

### 2. Modelagem Preditiva
**Objetivo**: Desenvolver modelos para prever custos e identificar drivers

**Algoritmos testados**:
- Regressão Linear (baseline)
- Random Forest Regressor

**Métricas de avaliação**:
- Mean Squared Error (MSE)
- R² Score
- Validação cruzada

### 3. Análise de Performance
**Objetivo**: Identificar padrões de eficiência/ineficiência

**Indicadores calculados**:
- Custo por KM
- Margem operacional
- Entregas por dia
- Eficiência de rotas

## 🔍 Pressupostos da Análise

1. **Consistência dos dados**: Os registros refletem a operação real
2. **Completude**: Dados suficientes para inferências estatísticas
3. **Estacionariedade**: Relações se mantêm no período analisado

## ⚠️ Limitações

- Período limitado (9 meses)
- Variáveis externas não capturadas (trânsito, clima)
- Dados agregados podem ocultar variações específicas

## 🛠️ Ferramentas Utilizadas

- **Python 3.8+**
- **Pandas**: Manipulação de dados
- **Scikit-learn**: Modelagem
- **Matplotlib/Seaborn**: Visualizações
- **Jupyter**: Análise interativa

## ✅ Validações Realizadas

1. **Split treino/teste**: 80/20 com random state fixo
2. **Comparação de modelos**: Múltiplos algoritmos
3. **Análise de resíduos**: Verificação de pressupostos
4. **Importância de features**: Identificação de drivers principais
