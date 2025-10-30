from fastapi import FastAPI
from app.routes import data_routes, employees
from app.database import create_tables

app = FastAPI(title="DataFlow Manager")

# Crear tablas al iniciar
create_tables()

# Registrar rutas
app.include_router(data_routes.router)
app.include_router(employees.router)

@app.get("/")
def home():
    return {"message": "Bienvenido a DataFlow Manager API 😎"}
