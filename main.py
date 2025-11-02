from fastapi import FastAPI
from routers import employees

app = FastAPI(
    title="DataFlow Manager",
    description="App para practicar FastAPI y gestión de datos",
    version="0.1"
)

# Rutas
app.include_router(employees.router)

@app.get("/", tags=["Root"])
def home():
    return {"message": "Bienvenido a DataFlow Manager 🚀"}