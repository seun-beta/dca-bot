import os
from peewee import (
    Model,
    DateTimeField,
    CharField,
    FloatField,
    PostgresqlDatabase,
)


db = PostgresqlDatabase(os.environ.get("DATABASE_URI"))


class BaseModel(Model):
    created_on = DateTimeField()
    updated_on = DateTimeField()


class Transaction(BaseModel):
    from_currency = CharField()
    to_currency = CharField()
    amount = FloatField()

    class Meta:
        database = db


db.connect()
db.create_tables([Transaction])
