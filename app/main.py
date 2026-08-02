from fastapi import FastAPI

from .routers import health,tickets


app = FastAPI(title="SupportDesk API")


@app.get("/")
def home():
    return {"message":"Hey im learning fastapi"}


app.include_router(health.router)
app.include_router(tickets.router)