from src.services.database import db, Transaction


def create_tables():
    with db:
        db.create_tables([Transaction])
