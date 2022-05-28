from services.models import db, Transaction


MODELS = Transaction


def recreate_tables():
    db.drop_tables(MODELS)
    db.create_tables(MODELS)
