import streamlit as st
import pandas as pd
from services.api_client import get_products

st.title("📋 Listado de productos")

products = get_products() #Con Get_products de api_client.py se hace el GET

if not products:
    st.info("No hay productos registrados")
else:
    df = pd.DataFrame(products)

    st.subheader("Tabla de productos")
    st.dataframe(df, use_container_width=True)

    st.subheader("Resumen")
    col1, col2 = st.columns(2)

    col1.metric("Total productos", len(df))
    col2.metric("Precio promedio", round(df["price"].mean(), 2))
