from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from src.routes.auth.main import router as auth_router
from src.routes.authors.main import router as authors_router
from src.routes.books.main import router as books_router
from src.routes.images.main import router as images_router
from src.routes.publishers.main import router as publishers_router
from src.routes.categories.main import router as categories_router
from src.routes.subcategories.main import router as subcategories_router
from src.routes.languages.main import router as languages_router
from src.routes.users.main import router as users_router
from src.config.security import validate_token

app = FastAPI()
app.include_router(auth_router)
app.include_router(authors_router)
app.include_router(books_router)
app.include_router(images_router)
app.include_router(publishers_router)
app.include_router(categories_router)
app.include_router(subcategories_router)
app.include_router(languages_router)
app.include_router(users_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def jwt_filter(request, call_next):
    return await validate_token(request, call_next)

@app.get("/")
def main_route():
    return RedirectResponse(url="/docs")
