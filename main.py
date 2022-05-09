from fastapi import FastAPI


from db import models, database
from db.database import engine
from routes import users, posts

app = FastAPI()


app.include_router(users.router)
app.include_router(posts.router)
