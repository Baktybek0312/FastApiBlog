from fastapi import FastAPI

from post_app import models
from post_app.database import engine
from post_app.routes import users, posts

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(posts.router)
