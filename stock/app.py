from config import *


query = Produtos.select().where(Produtos.stock < 10)
st.markdown(f"""
#### ESTOQUE BAIXO: {len(query)}
""")

query = Produtos.select().where(Produtos.stock == 0)
st.markdown(f"""
#### SEM ESTOQUE: {len(query)}
""")

active = Produtos.select().where(Produtos.status == "ATIVO")
desactive = Produtos.select().where(Produtos.status == "INATIVO")
st.markdown(f"""
#### ATIVOS: {len(active)}
#### INATIVOS: {len(desactive)}
""")
