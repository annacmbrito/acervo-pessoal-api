from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def main_route():
    return RedirectResponse(url="/docs")