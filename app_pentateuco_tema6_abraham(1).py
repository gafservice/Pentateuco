
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Evaluación: Abraham (Génesis 12–25)", layout="wide")
st.title("📘 Evaluación: Abraham (Génesis 12–25)")
st.markdown("Lectura recomendada: Génesis 12–25 y páginas 48–58 del libro *El Pentateuco* de Pablo Hoff.")

with open("evaluacion_pentateuco_tema6_abraham_30preguntas.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1800, scrolling=True)
