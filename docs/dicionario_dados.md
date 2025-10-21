# 📚 Dicionário de Dados

## 📊 dados_logistica.csv (Dados Diários)

| Variável | Tipo | Descrição | Unidade |
|----------|------|-----------|---------|
| Data | Date | Data da operação | YYYY-MM-DD |
| Custo Combustível | Numeric | Custo total com combustível | R$ |
| Custo Manutenção | Numeric | Custo total com manutenção | R$ |
| Custo Motorista | Numeric | Custo total com motoristas | R$ |
| Custo Total | Numeric | Soma de todos os custos | R$ |
| KM Percorridos | Numeric | Quilômetros percorridos no dia | km |
| Entregas | Integer | Número de entregas realizadas | unidades |
| Peso (ton) | Numeric | Peso total transportado | toneladas |
| Frete | Numeric | Valor total do frete | R$ |
| Margem | Numeric | Margem bruta (Frete - Custo Total) | R$ |
| Margem % | Numeric | Margem percentual | % |
| Custo/KM | Numeric | Custo por quilômetro percorrido | R$/km |
| Entregas/Dia | Numeric | Entregas por dia (redundante) | unidades |
| KM/Entrega | Numeric | Quilômetros por entrega | km/unidade |
| Mês | String | Mês de referência | YYYY-MM |

## 📈 dados_mensais.csv (Dados Mensais)

| Variável | Tipo | Descrição |
|----------|------|-----------|
| Mês | String | Mês de referência |
| Custo Total | Numeric | Custo total mensal |
| Custo Combustível | Numeric | Custo com combustível mensal |
| Custo Manutenção | Numeric | Custo com manutenção mensal |
| Custo Motorista | Numeric | Custo com motoristas mensal |
| Frete | Numeric | Faturamento com fretes mensal |
| Margem | Numeric | Margem bruta mensal |
| KM Percorridos | Numeric | Quilômetros percorridos mensais |
| Entregas | Integer | Total de entregas mensais |
| Peso (ton) | Numeric | Peso total transportado mensal |
| Margem % | Numeric | Margem percentual mensal |
| Custo/KM | Numeric | Custo médio por km mensal |

## 🎯 tabela_acoes.csv (Plano de Ações)

| Variável | Tipo | Descrição |
|----------|------|-----------|
| ID | String | Identificador único da ação |
| Ação | String | Descrição da ação |
| Prioridade | String | Urgente/Prioritária/Planejada |
| Impacto | Numeric | Impacto financeiro esperado (R$) |
| Esforço | Numeric | Esforço necessário (0-100) |
| Prazo | Integer | Prazo estimado em dias |
| Status | String | Status atual da ação |

## 🔍 Observações

- **Dados diários**: 273 registros (Jan-Set 2024)
- **Dados mensais**: 9 registros (Jan-Set 2024)
- **Ações**: 10 ações prioritárias
- **Consistência**: Dados validados e consistentes
