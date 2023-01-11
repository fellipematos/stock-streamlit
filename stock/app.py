from config import *


infoCol1, infoCol2, infoCol3 = st.columns(3)
with infoCol1:
    st.text("ESTOQUE BAIXO")

with infoCol2:
    st.text("SEM ESTOQUE")

with infoCol3:
    st.text("ATIVOS 200")
    st.text("INATIVOS 300")
