from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = "postgresql://postgres:root_db@localhost:5432/prog_4_db"

engine = create_engine(DATABASE_URL, echo=True)


def create_table_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
