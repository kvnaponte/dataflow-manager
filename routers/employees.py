from fastapi import APIRouter, Form
from typing import List
import json
import os
from models.employee import Employee

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

DATA_FILE = "data/employees.json"

# Helper para leer el archivo JSON
def read_data():
    if not os.path.exists(DATA_FILE):
        return []
    
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except:
            return []

# Helper para guardar datos
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

@router.post("/", summary="Create Employee")
def create_employee(
    name: str = Form(...),
    position: str = Form(...),
    department: str = Form(...),
    email: str = Form(...)
):
    employees = read_data()

    # mini lógica amateur: asignar ID incremental
    new_id = len(employees) + 1  

    new_employee = {
        "id": new_id,
        "name": name,
        "position": position,
        "department": department,
        "email": email
    }

    employees.append(new_employee)
    save_data(employees)

    return {
        "message": "Empleado registrado con éxito 🎯",
        "data": new_employee
    }

@router.get("/", summary="Get Employees")
def get_employees() -> List[Employee]:
    return read_data()

@router.put("/{employee_id}", summary="Update Employee")
def update_employee(
    employee_id: int,
    name: str = Form(None),
    position: str = Form(None),
    department: str = Form(None),
    email: str = Form(None),
):
    employees = read_data()

    # buscar empleado
    for emp in employees:
        if emp["id"] == employee_id:
            if name: emp["name"] = name
            if position: emp["position"] = position
            if department: emp["department"] = department
            if email: emp["email"] = email
            
            save_data(employees)

            return {
                "message": "Empleado actualizado ✅",
                "data": emp
            }

    return {"error": "Empleado no encontrado ❌"}

@router.delete("/{employee_id}", summary="Delete Employee")
def delete_employee(employee_id: int):
    employees = read_data()

    for emp in employees:
        if emp["id"] == employee_id:
            employees.remove(emp)
            save_data(employees)

            return {"message": "Empleado eliminado 🗑️"}

    return {"error": "Empleado no encontrado ❌"}
