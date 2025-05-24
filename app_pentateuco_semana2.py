
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Pentateuco – Semana 2", layout="wide")
st.title("📘 Evaluaciones – Semana 2")
st.markdown("Lectura sugerida: Génesis 12–50 y páginas 48–103 del libro *El Pentateuco* de Pablo Hoff.")
st.markdown("---")

temas = {
    "Tema 6 – Abraham (Gén. 12–25)": "evaluacion_pentateuco_tema6_abraham_30preguntas.html",
    "Tema 7 – Agar e Ismael": "evaluacion_pentateuco_tema7_agar_ismael.html",
    "Tema 8 – Abraham y Abimelec / Isaac e Ismael": "evaluacion_pentateuco_tema8_abimelec_isaac.html",
    "Tema 9 – Isaac y Jacob": "evaluacion_pentateuco_tema9_isaac_jacob.html",
    "Tema 10 – Jacob en Canaán": "evaluacion_pentateuco_tema10_jacob_canaan.html",
    "Tema 11 – José (Gén. 37–50)": "evaluacion_pentateuco_tema11_jose.html",
    "Tema 12 – José en Egipto": "evaluacion_pentateuco_tema12_jose_egipto.html"
}

seleccion = st.selectbox("Seleccione el tema para evaluar:", list(temas.keys()))

if seleccion:
    archivo = temas[seleccion]
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            html_content = f.read()
        components.html(html_content, height=1800, scrolling=True)
    except FileNotFoundError:
        st.warning(f"⚠️ El archivo '{archivo}' aún no ha sido generado.")
