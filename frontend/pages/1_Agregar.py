import streamlit as st
from services.api_client import create_product

st.title("➕ Agregar producto")

with st.form("product_form"):
    name = st.text_input("Nombre del producto")
    price = st.number_input("Precio", min_value=0.0, step=0.5)

    submitted = st.form_submit_button("Guardar")

    if submitted:
        if not name:
            st.warning("El nombre es obligatorio")
        else:
            create_product(name, price) #Con Create_product de api_client.py se hace el POST
            st.success("Producto agregado correctamente 🎉")
