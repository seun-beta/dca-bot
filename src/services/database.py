import sqlite3
from peewee import Model, DateTimeField, CharField, FloatField, SqliteDatabase

from services.constants import DATABASE_NAME

db = SqliteDatabase(DATABASE_NAME)


class BaseModel(Model):
    created_on = DateTimeField()
    updated_on = DateTimeField()

    class Meta:
        database = db


class Transaction(BaseModel):
    from_currency = CharField()
    to_currency = CharField()
    amount = FloatField()


connection = sqlite3.connect("dca.sqlite3")
cur = connection.cursor()

cur.execute()

connection.commit()
