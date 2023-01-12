from config import *
from datetime import datetime


st.markdown("# Cadastro de Produto")

getData = datetime.now().strftime("%d%m%Y %H:%M:%S")

with st.form("formNewProduct"):
    sku = st.text_input("SKU", max_chars=25)
    name = st.text_input("Nome", max_chars=60)
    stock = st.number_input("Estoque", min_value=0, max_value=9999)
    status = st.radio("Status", options=["ATIVO", "INATIVO"], horizontal=True, label_visibility="hidden")
    dateCreated = getData
    lastUpdated = dateCreated

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        new = Produtos(sku=sku, name=name, stock=stock, status=status, dateCreated=dateCreated, lastUpdated=lastUpdated)
        new.save()
