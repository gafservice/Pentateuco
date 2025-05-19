
import streamlit as st

st.set_page_config(page_title="Evaluación Pentateuco - Semana 1", layout="centered")

st.title("📘 Evaluación del Pentateuco - Semana 1")
st.markdown("Instituto Bíblico de las Asambleas de Dios – IBAD")
st.markdown("---")

st.header("Seleccione un tema para iniciar la evaluación:")

col1, col2 = st.columns(2)

with col1:
    st.markdown('[📝 Tema 1: Introducción y Autoría](evaluacion_pentateuco_tema1_aleatorio_global.html)', unsafe_allow_html=True)
    st.markdown('[🌍 Tema 2: La Creación](evaluacion_pentateuco_tema2_creacion_global.html)', unsafe_allow_html=True)
    st.markdown('[🍎 Tema 3: La Caída](evaluacion_pentateuco_tema3_caida_global.html)', unsafe_allow_html=True)

with col2:
    st.markdown('[🌊 Tema 4: El Diluvio](evaluacion_pentateuco_tema4_diluvio_global.html)', unsafe_allow_html=True)
    st.markdown('[🌐 Tema 5: La Dispersión](evaluacion_pentateuco_tema5_dispersion_global.html)', unsafe_allow_html=True)

st.markdown("---")
st.info("Cada enlace abrirá el formulario correspondiente en una nueva pestaña del navegador. Al terminar todos, podrás calcular la nota global en el formulario principal.")

st.markdown('[🔗 Abrir Panel Global para calcular nota final](index_semana1_global.html)', unsafe_allow_html=True)
