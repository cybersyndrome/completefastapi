from fastapi import FastAPI, Depends
import models
from database import engine, sessionLocal
from routers import auth, todos, users
from starlette.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

#mounting adding completely different sub applicatioin
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(auth.router) 
app.include_router(todos.router)
app.include_router(users.router)
# app.include_router(address.router)
