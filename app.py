import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="Mi App Streamlit",
    page_icon="🚀",
    layout="wide"
)

# Título principal
st.title("🚀 Mi Primera App Streamlit en Docker Mili <3")
st.markdown("---")

# Sidebar
st.sidebar.header("Configuración")
nombre = st.sidebar.text_input("Tu nombre:", "Usuario")
edad = st.sidebar.slider("Tu edad:", 1, 100, 25)

# Contenido principal
col1, col2 = st.columns(2)

with col1:
    st.header(f"¡Hola {nombre}!")
    st.write(f"Tienes {edad} años")
    
    # Botón interactivo
    if st.button("Generar datos aleatorios"):
        st.success("¡Datos generados exitosamente!")

with col2:
    st.header("📊 Gráfico de ejemplo")
    
    # Generar datos aleatorios
    data = pd.DataFrame({
        'x': range(10),
        'y': np.random.randn(10).cumsum(),
        'categoria': np.random.choice(['A', 'B', 'C'], 10)
    })
    
    # Crear gráfico
    fig = px.line(data, x='x', y='y', color='categoria', 
                  title="Datos Aleatorios")
    st.plotly_chart(fig, use_container_width=True)

# Métricas
st.markdown("---")
st.header("📈 Métricas")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Usuarios", "1,234", "12%")
with col2:
    st.metric("Ventas", "$5,678", "-2%")
with col3:
    st.metric("Conversión", "3.4%", "0.5%")
with col4:
    st.metric("Satisfacción", "4.8/5", "0.2")

# Tabla de datos
st.markdown("---")
st.header("📋 Tabla de Datos")
st.dataframe(data, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("**Aplicación creada con Streamlit y Docker** 🐳")
