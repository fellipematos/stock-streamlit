from peewee import SqliteDatabase, Model, CharField, IntegerField


database = SqliteDatabase("database.db")

class BaseModel (Model):
    class Meta:
        database = database

class Produtos(BaseModel):
    sku = CharField()
    name = CharField()
    status = IntegerField()
    stock = IntegerField()
    dateCreated = CharField(max_length=17)
    lastUpdated = CharField(max_length=17)

Produtos.create_table()
