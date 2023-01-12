from config import *
from datetime import datetime

getData = datetime.now().strftime("%d%m%Y %H:%M:%S")

sku = "SKU123"
name = "Produto Teste Modelo Form"
status = "ATIVO"
stock = 1
dateCreated = getData
lastUpdated = dateCreated

new = Produtos(sku=sku, name=name, stock=stock, status=status, dateCreated=dateCreated, lastUpdated=lastUpdated)
new.save()
st.balloons()
