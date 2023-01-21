import ormar
#import re
#from pydantic import validator
#from sqlalchemy.sql.expression import table
#from config.config import database, metadata


import databases
import sqlalchemy

metadata = sqlalchemy.MetaData()
database = databases.Database("postgresql+asyncpg://postgres:marc1307@localhost/postgres")

# bd_usuarios = "postgresql+asyncpg://" + userPostgres + ":" + passworldPostgres + "@" + host + "/" + bdname


class Usuario(ormar.Model):
    class Meta:
        metadata = metadata
        database = database
        tablename = "usuarios"

    id: int = ormar.Integer(primary_key=True)
    cpf: str = ormar.String(max_length=14)
    nome: str = ormar.String(max_length=100)
    email: str = ormar.String(max_length=100)
    telefone: str = ormar.String(max_length=50)




    


