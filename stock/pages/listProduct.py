from config import *


st.markdown("# Lista de Produto")

guide0, guide1, guide2 = st.tabs(["TODOS", "ATIVO", "INATIVO"])
with guide0:
   st.markdown("status - sku - title - stock - [action]")

with guide1:
   st.markdown("status - sku - title - stock - [action]")

with guide2:
   st.markdown("status - sku - title - stock - [action]")
