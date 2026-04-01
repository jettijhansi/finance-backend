from fastapi import FastAPI
from app.database import engine, Base
from app.routes import user, record, dashboard

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(record.router)
app.include_router(dashboard.router)

from fastapi.responses import HTMLResponse

@app.get("/")
def root():
    return {"message": "User + Record + Dashboard API working"}