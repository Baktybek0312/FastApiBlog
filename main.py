from fastapi import FastAPI


from db import models, database
from db.database import engine
from routes import users, posts

app = FastAPI()

# models.Base.metadata.create_all(bind=engine)


app.include_router(users.router)
app.include_router(posts.router)
