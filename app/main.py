from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import items, users
from app.database import engine, Base
from app import models

app = FastAPI()

Base.metadata.create_all(bild=engine)
# ===CORS===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===ROUTERS===
app.include_router(items.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Hello, World"}