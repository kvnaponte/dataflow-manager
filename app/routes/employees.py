from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from fastapi import Form

router = APIRouter(prefix="/employees", tags=["Employees"])

# 🧩 Modelo de entrada — lo que el usuario enviará en el body
class EmployeeIn(BaseModel):
    name: str
    role: str
    area: str
    salary: float

# 🧾 Modelo de salida — lo que la API devolverá como respuesta
class EmployeeOut(BaseModel):
    message: str
    data: EmployeeIn

# 📥 Base de datos temporal (solo para ejemplo)
employees_db: List[EmployeeIn] = []


# 🚀 Endpoint para agregar empleados
@router.post("/", response_model=EmployeeOut, summary="Add a new employee")
def add_employee(
    name: str = Form(...),
    role: str = Form(...),
    area: str = Form(...),
    salary: float = Form(...)
):
    """
    Add a new employee to the database.
    """
    emp = EmployeeIn(name=name, role=role, area=area, salary=salary)
    employees_db.append(emp)
    return {
        "message": f"Employee {emp.name} added successfully.",
        "data": emp
    }



# 📄 Endpoint para obtener todos los empleados
@router.get("/", response_model=List[EmployeeIn], summary="Get all employees")
def get_employees():
    """
    Retrieve a list of all employees.
    """
    return employees_db
