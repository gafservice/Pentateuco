
import streamlit as st

st.set_page_config(page_title="Pentateuco - Evaluación General", layout="centered")

st.title("📚 Evaluaciones por Semana – Pentateuco IBAD")
st.markdown("**Curso: Pentateuco | Instituto Bíblico de las Asambleas de Dios**")
st.markdown("---")

semanas = [
    ("Semana 1", "12–18 mayo", "Introducción Génesis, Caída, Dispersión", "app_pentateuco_semana1.py"),
    ("Semana 2", "19–25 mayo", "Historia Patriarcal", "app_pentateuco_semana2.py"),
    ("Semana 3", "26 mayo – 01 junio", "Introducción al Éxodo / Egipto / Sinaí", None),
    ("Semana 4", "02–08 junio", "Pacto en el Sinaí, Tabernáculo", None),
    ("Semana 5", "09–15 junio", "Levítico, Sacerdocio", None),
    ("Semana 6", "16–22 junio", "Purificación, Fiestas Solemnes", None),
    ("Semana 7", "23–29 junio", "Censos, Organización, Cades Barnea", None),
    ("Semana 8", "30 junio – 06 julio", "Rebelión de Coré, viaje a Moab", None),
    ("Semana 9", "07–13 julio", "Deuteronomio, Diez Mandamientos", None),
    ("Semana 10", "14–20 julio", "Profecías sobre el Futuro de Israel", None)
]

for nombre, fechas, tema, archivo in semanas:
    with st.expander(f"📘 {nombre} ({fechas})"):
        st.markdown(f"**Tema:** {tema}")
        if archivo:
            st.markdown(f"[👉 Iniciar evaluación]({archivo})", unsafe_allow_html=True)
        else:
            st.markdown("⏳ *Evaluación próximamente disponible*")
