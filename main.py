from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from starlette.responses import RedirectResponse
from src.routes.auth.main import router as auth_router
from src.routes.users.main import router as users_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(users_router)

@app.get("/")
def main_route():
    return RedirectResponse(url="/docs")