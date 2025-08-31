from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from time import sleep
# import psycopg2
# from psycopg2.extras import RealDictCursor


# while True:
#     try:
#         conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="1234", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print()
#         print("[INFO] --- Database connection was successfull ✅")
#         print()
#         break
#     except Exception as error:
#         print("[INFO] --- Connecting to database was failed ❌")
#         print("Error: ", error)
#         sleep(3)



SQLALCHEMY_DATABSE_URL = 'postgresql://postgres:1234@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABSE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

