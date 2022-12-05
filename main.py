from fastapi import FastAPI, status
from db import models
from db.database import engine
from routes import users_route, notes_route
from auth import authentication

app = FastAPI(
    "title":"A note keeping web API"
)

@app.get("/")
def index():
    return {"status": status.HTTP_200_OK}


app.include_router(users_route.router)
app.include_router(notes_route.router)
app.include_router(authentication.router)



models.Base.metadata.create_all(engine)
