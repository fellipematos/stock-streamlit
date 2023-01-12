from config import *


st.markdown("## Lista de Produto")

guide0, guide1, guide2 = st.tabs(["TODOS", "ATIVO", "INATIVO"])
with guide0:
   query = Produtos.select().where(Produtos.status != None)
   for pro in query:
      st.write(pro.sku, pro.sku, pro.name)

with guide1:
   query = Produtos.select().where(Produtos.status == "ATIVO")
   for pro in query:
      st.write(pro.sku, pro.sku, pro.name)

with guide2:
   query = Produtos.select().where(Produtos.status == "INATIVO")
   for pro in query:
      st.write(pro.sku, pro.sku, pro.name)
