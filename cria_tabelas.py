from typing import Optional

import databases
import pydantic

import ormar
import sqlalchemy

DATABASE_URL = "postgresql://postgres:marc1307@localhost/postgres"
database = databases.Database("postgresql://postgres:marc1307@localhost/postgres")
metadata = sqlalchemy.MetaData()


# note that this step is optional -> all ormar cares is a internal
# class with name Meta and proper parameters, but this way you do not
# have to repeat the same parameters if you use only one database
class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


# Note that all type hints are optional
# below is a perfectly valid model declaration
# class Author(ormar.Model):
#     class Meta(BaseMeta):
#         tablename = "authors"
#
#     id = ormar.Integer(primary_key=True) # <= notice no field types
#     name = ormar.String(max_length=100)


class Author(ormar.Model):
    class Meta(BaseMeta):
        tablename = "authors"

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100)


class Book(ormar.Model):
    class Meta(BaseMeta):
        tablename = "books"

    id: int = ormar.Integer(primary_key=True)
    author: Optional[Author] = ormar.ForeignKey(Author)
    title: str = ormar.String(max_length=100)
    year: int = ormar.Integer(nullable=True)


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





# create the database
# note that in production you should use migrations
# note that this is not required if you connect to existing database
engine = sqlalchemy.create_engine(DATABASE_URL)
# just to be sure we clear the db before
metadata.drop_all(engine)
metadata.create_all(engine)