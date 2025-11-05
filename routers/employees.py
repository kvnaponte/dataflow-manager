from fastapi import APIRouter, HTTPException, Form
from typing import List
from models.employee import Employee, EmployeeCreate, EmployeeResponse
import os, json

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)

DATA_FILE = "data/employees.json"

def read_data():
    if not os.path.exists(DATA_FILE):
        return []
    
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except:
            return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

@router.post("/", response_model=EmployeeResponse, summary="Create Employee")
def create_employee(employee: EmployeeCreate):
    employees = read_data()
    new_id = len(employees) + 1

    new_employee = {
        "id": new_id,
        "name": employee.name,
        "position": employee.position,
        "department": employee.department,
        "email": employee.email
    }

    employees.append(new_employee)
    save_data(employees)

    return new_employee

@router.get("/", response_model=List[EmployeeResponse], summary="Get Employees")
def get_employees():
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

    for emp in employees:
        if emp["id"] == employee_id:
            if name: emp["name"] = name
            if position: emp["position"] = position
            if department: emp["department"] = department
            if email: emp["email"] = email
            
            save_data(employees)
            return {"message": "Empleado actualizado ✅", "data": emp}

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
