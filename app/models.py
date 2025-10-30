from pydantic import BaseModel

# Modelo Pydantic para la entrada de datos
class EmployeeIn(BaseModel):
    name: str
    role: str
    area: str
    salary: float


# Clase auxiliar para manejar la lógica de los empleados
class Employee:
    def __init__(self, name, role, area, salary):
        self.name = name
        self.role = role
        self.area = area
        self.salary = salary

    def to_dict(self):
        return {
            "name": self.name,
            "role": self.role,
            "area": self.area,
            "salary": self.salary
        }
