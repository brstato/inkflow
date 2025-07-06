from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.controllers import page_controller


app = FastAPI(
    title="InkFlow"
)


app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(page_controller.router)


@app.get("/health", tags=["Status"])
def health_check():
    return {"status": "ok"}