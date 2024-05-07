from fastapi import Request, status
from fastapi.responses import JSONResponse
from src.routes.commons.jwt_service import jwt

async def validate_token(request: Request, call_next):
    path = request.url.path + ('' if request.url.path.endswith('/') else '/')
    method = request.method
    bearer = request.headers.get('Authorization')

    white_list = [
        {"method": "GET", "path": "/"},
        {"method": "GET", "path": "/docs/"},
        {"method": "GET", "path": "/openapi.json/"},
        {"method": "POST", "path": "/api/v1/auth/"},
        {"method": "POST", "path": "/api/v1/users/"}
    ]

    if {"method": method, "path": path} not in white_list:

        if not bearer or not bearer.lower().startswith('bearer '):
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={"detail":"Invalid token"}
            )
        
        token = bearer.split()[1]

        try:
            jwt.get_user_email(token)
        except Exception as e:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                content={"detail":e.args[0]}
            )
    
    return await call_next(request)