from sqlmodel import SQLModel, Session, create_engine

engine = create_engine("postgresql://postgres:password@143.244.169.231:5432/grocery_shop_backend")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
