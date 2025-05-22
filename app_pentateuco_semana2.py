
import streamlit as st

st.set_page_config(page_title="Evaluación Pentateuco - Semana 2", layout="centered")

st.title("📘 Evaluación del Pentateuco - Semana 2")
st.markdown("Instituto Bíblico de las Asambleas de Dios – IBAD")
st.markdown("---")

st.header("Seleccione un tema para iniciar la evaluación:")

col1, col2 = st.columns(2)

with col1:
    st.markdown('[📝 Tema 1: Abraham (Gn. 12–20)](evaluacion_pentateuco_semana2_tema1.html)', unsafe_allow_html=True)
    st.markdown('[📝 Tema 2: Abraham (Gn. 21–25)](evaluacion_pentateuco_semana2_tema2.html)', unsafe_allow_html=True)
    st.markdown('[📝 Tema 3: Isaac y Jacob](evaluacion_pentateuco_semana2_tema3.html)', unsafe_allow_html=True)

with col2:
    st.markdown('[📝 Tema 4: Jacob (Gn. 29–36)](evaluacion_pentateuco_semana2_tema4.html)', unsafe_allow_html=True)
    st.markdown('[📝 Tema 5: José (Gn. 37–41)](evaluacion_pentateuco_semana2_tema5.html)', unsafe_allow_html=True)
    st.markdown('[📝 Tema 6: José y Jacob](evaluacion_pentateuco_semana2_tema6.html)', unsafe_allow_html=True)

st.markdown("---")
st.info("Cada enlace abrirá el formulario correspondiente en una nueva pestaña del navegador. Al terminar todos, podrás calcular la nota global en el formulario principal.")

st.markdown('[🔗 Abrir Panel Global para calcular nota final](index_semana2_global.html)', unsafe_allow_html=True)
