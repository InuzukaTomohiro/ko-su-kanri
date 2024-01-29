from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# _database_url = URL.create(
#     drivername="mysql+mysqldb",
#     username=Env.DATABASE_USER,
#     password=Env.DATABASE_PASSWORD,
#     host=Env.DATABASE_HOST,
#     port=Env.DATABASE_PORT,
#     database=Env.DATABASE_NAME
# )

Engine = create_engine("mysql+mysqldb://user:password@mysql/ko_su_kanri", echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()