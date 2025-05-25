
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Evaluaciones Pentateuco", layout="wide")
st.title("📘 Evaluaciones del Pentateuco")
st.markdown("Seleccione una semana para acceder a sus formularios:")

semanas = {
    "Semana 1": {
        "Tema 1: Introducción y Autoría": "evaluacion_pentateuco_tema1_aleatorio_global.html",
        "Tema 2: La Creación": "evaluacion_pentateuco_tema2_creacion_global.html",
        "Tema 3: La Caída": "evaluacion_pentateuco_tema3_caida_global.html",
        "Tema 4: El Diluvio": "evaluacion_pentateuco_tema4_diluvio_global.html",
        "Tema 5: La Dispersión": "evaluacion_pentateuco_tema5_dispersion_global.html"
    },
    "Semana 2": {
        "Tema 6 – Abraham": "evaluacion_pentateuco_semana2_tema6.html",
        "Tema 7 – Agar e Ismael": "evaluacion_pentateuco_semana2_tema7.html",
        "Tema 8 – Abraham y Abimelec": "evaluacion_pentateuco_semana2_tema8.html",
        "Tema 9 – Isaac y Jacob": "evaluacion_pentateuco_semana2_tema9.html",
        "Tema 10 – Jacob en Canaán": "evaluacion_pentateuco_semana2_tema10.html",
        "Tema 11 – Regreso y Esaú": "evaluacion_pentateuco_semana2_tema11.html",
        "Tema 12 – José en Egipto": "evaluacion_pentateuco_semana2_tema12.html"
    }
}

semana_seleccionada = st.selectbox("📅 Seleccione la semana", list(semanas.keys()))

if semana_seleccionada:
    temas = semanas[semana_seleccionada]
    tema_seleccionado = st.selectbox("📝 Seleccione el tema a evaluar:", list(temas.keys()))
    if tema_seleccionado:
        archivo = temas[tema_seleccionado]
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                html_content = f.read()
            components.html(html_content, height=1800, scrolling=True)
        except FileNotFoundError:
            st.warning(f"⚠️ El archivo '{archivo}' no se encuentra en el directorio actual.")
