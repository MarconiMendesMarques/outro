import databases
import sqlalchemy
import os

# bd_usuarios = "postgresql+asyncpg://" + userPostgres + ":" + passworldPostgres + "@" + host + "/" + bdname
metadata = sqlalchemy.MetaData()
database = databases.Database("postgresql+asyncpg://postgres:marc1307@localhost/postgres")



#DATABASE_URL = "postgresql+asyncpg://postgres:marc1307@localhost/postgres"
#DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+asyncpg://postgres:marc1307@localhost/postgres')
#DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+asyncpg://postgres:marc1307@localhost:5432/teste')
#postgresql://postgres:marc1307@localhost/postgres
#TEST_DATABASE = os.getenv('TEST_DATABASE', 'false') in ('true', 'yes')
#database = databases.Database(DATABASE_URL, force_rollback=TEST_DATABASE)
#metadata = sqlalchemy.MetaData()
