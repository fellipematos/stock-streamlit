from config import *
from datetime import datetime


st.markdown("# Cadastro de Produto")

getData = datetime.now().strftime("%d%m%Y %H:%M:%S")

with st.form(key="insertProduct"):
    col1, col2 = st.columns(2)
    with col1:
        sku = st.text_input("SKU", max_chars=25)
        name = st.text_input("Nome", max_chars=60)
    with col2:
        stock = st.number_input("Estoque", min_value=0, max_value=9999)
        status = st.radio("Status", options=["ATIVO", "INATIVO"], horizontal=True, label_visibility="hidden")
        
    st.form_submit_button("Salvar Produto")
