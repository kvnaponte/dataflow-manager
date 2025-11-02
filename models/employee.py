from pydantic import BaseModel

# Base del empleado (datos comunes)
class EmployeeBase(BaseModel):
    name: str
    position: str
    department: str
    email: str

# Modelo usado para crear un empleado
class EmployeeCreate(EmployeeBase):
    pass

# Modelo de empleado completo con id
class Employee(EmployeeBase):
    id: int
