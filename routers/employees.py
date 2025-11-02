from fastapi import APIRouter, HTTPException
from typing import List
from models.employee import Employee, EmployeeCreate
from utils.json_utils import read_data, save_data
import uuid

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/", response_model=Employee)
def create_employee(employee: EmployeeCreate):
    data = read_data()

    new_employee = {
        "id": str(uuid.uuid4()),
        "name": employee.name,
        "role": employee.role,
        "department": employee.department
    }

    data.append(new_employee)
    save_data(data)
    return new_employee


@router.get("/", response_model=List[Employee])
def get_employees():
    data = read_data()
    return data
