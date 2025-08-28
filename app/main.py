from typing import List
from fastapi import FastAPI, status, HTTPException, Response, Depends
from fastapi.params import Body
from pydantic import BaseModel
# import psycopg2
# from psycopg2.extras import RealDictCursor
from time import sleep
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user




models.Base.metadata.create_all(bind=engine)



app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)



@app.get("/")
async def root():
    return {"message": "Hello world"}




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
