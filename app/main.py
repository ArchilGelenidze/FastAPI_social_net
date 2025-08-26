from fastapi import FastAPI, status, HTTPException, Response
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
from time import sleep

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True

while True:
    try:
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="1234", cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print()
        print("[INFO] --- Database connection was successfull ✅")
        print()
        break
    except Exception as error:
        print("[INFO] --- Connecting to database was failed ❌")
        print("Error: ", error)
        sleep(3)



@app.get("/")
async def root():
    return {"message": "Hello world"}




@app.get("/posts")
async def get_posts():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    return {"data": posts}



@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *;""",
                    (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"data": new_post}




@app.get("/posts/{id}")
async def get_post(id: int):
    cursor.execute("""SELECT * FROM posts WHERE id = %s;""", (str(id),))      # It is said that this comma saves you from some issues
    post = cursor.fetchone()
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id {id} was not found")

    return {"post_detail": post}



@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *;""", (str(id),))
    deleted_post = cursor.fetchone()

    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    conn.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)



@app.put("/posts/{id}")
async def update_post(id: int, post: Post):
    cursor.execute(
        """UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *;""", 
        (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()

    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")
    conn.commit()
    
    return {"data": updated_post}