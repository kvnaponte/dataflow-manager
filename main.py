from fastapi import FastAPI
from routers import employees, data_routes

app = FastAPI(
    title="DataFlow Manager",
    description="App para practicar FastAPI y gestión de datos",
    version="0.1"
)

app.include_router(employees.router)
app.include_router(data_routes.router)

@app.get("/", tags=["Root"])
def home():
    return {"message": "Bienvenido a DataFlow Manager 🚀"}
