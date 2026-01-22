import streamlit as st

st.set_page_config(
    page_title="Mini Fullstack",
    page_icon="📦",
    layout="centered"
)

st.title("📦 Mini Sistema de Productos")

st.markdown("""
Este es un **ejemplo educativo** usando:

- 🧠 **FastAPI** como backend  
- 🎨 **Streamlit** como frontend  
- 🗄 **SQLite** como base de datos  

### ¿Qué puedes hacer?
- Agregar productos
- Ver el listado
- Entender la comunicación frontend ↔ backend
""")

st.info("Usa el menú lateral para navegar entre páginas 👈")
