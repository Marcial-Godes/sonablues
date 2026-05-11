from sqlmodel import SQLModel, Session, create_engine


DATABASE_URL = "sqlite:///sonablues.db"


engine = create_engine(
    DATABASE_URL,
    echo=True,
)


def create_db():

    SQLModel.metadata.create_all(engine)


def get_session():

    return Session(engine)