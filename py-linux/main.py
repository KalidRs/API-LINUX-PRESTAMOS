from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware

from routes.usersRoutes import user, auth_router
from routes.materialRoutes import material
from routes.loanRoutes import loan

app = FastAPI(
    title="API",
    description="API de pruebas con rutas protegidas"
)

# Middleware CORS y ruta para front
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://front-prestamos.vercel.app/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Autenticación con HTTPBearer
security = HTTPBearer()

# Incluir routers
app.include_router(user)
app.include_router(auth_router)
app.include_router(material)
app.include_router(loan)
