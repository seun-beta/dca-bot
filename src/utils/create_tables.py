from services.models import *


def create_tables():
    with db:
        db.create_tables([Transaction])
