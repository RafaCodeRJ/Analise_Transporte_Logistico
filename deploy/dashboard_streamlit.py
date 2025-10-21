# Exemplo simplificado
import streamlit as st
from src.data_loader import carregar_dados_diarios

df = carregar_dados_diarios()
st.line_chart(df.set_index('Data')['Custo Total'])
