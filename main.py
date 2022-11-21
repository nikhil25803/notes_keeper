from fastapi import FastAPI, status
from db import models
from db.database import engine
from routes import users_route, notes_route

app = FastAPI()


@app.get('/')
def index():
    return {"status":status.HTTP_200_OK}

app.include_router(users_route.router)
app.include_router(notes_route.router)


models.Base.metadata.create_all(engine)