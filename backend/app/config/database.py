from sqlalchemy import MetaData
from databases import Database
from decouple import config
from sqlalchemy.ext.asyncio import create_async_engine


DATABASE_URL = f"mssql+pyodbc://{config('DATABASE_USER')}:{config('DATABASE_PASSWORD')}@{config('DATABASE_HOST')}/{config('DATABASE_NAME')}?driver=ODBC+Driver+17+for+SQL+Server"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_async_engine(DATABASE_URL, echo=True)
