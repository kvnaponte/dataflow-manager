from pydantic import BaseModel, EmailStr, Field

class EmployeeBase(BaseModel):
    name: str = Field(..., min_length=2, description="Nombre completo")
    position: str = Field(..., min_length=2, description="Cargo")
    department: str = Field(..., min_length=2, description="Departamento")
    email: EmailStr = Field(..., description="Correo")

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int

# Para evitar errores raros de import
class Employee(EmployeeResponse):
    pass

__all__ = ["Employee", "EmployeeCreate", "EmployeeResponse"]
