from config import *
from datetime import datetime


st.markdown("# Cadastro de Produto")

getData = datetime.now().strftime("%d%m%Y %H:%M:%S")

query = Produtos.select().where(Produtos.id == 2)
for pro in query:

    if pro.status == "ATIVO":
        index = 0
    elif pro.status == "INATIVO":
        index = 1

    with st.form("formNewProduct"):
        sku = st.text_input("SKU", max_chars=25, value=pro.id)
        name = st.text_input("Nome", max_chars=60, value=pro.name)
        stock = st.number_input("Estoque", min_value=0, max_value=9999, value=pro.stock)
        status = st.radio("Status", options=["ATIVO", "INATIVO"], index=index, horizontal=True, label_visibility="hidden")
        dateCreated = getData
        lastUpdated = dateCreated

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            new = Produtos(sku=sku, name=name, stock=stock, status=status, dateCreated=dateCreated, lastUpdated=lastUpdated)
            new.save()
