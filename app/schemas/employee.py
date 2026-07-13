from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class EmployeeBase(BaseModel):
    employee_id: str
    username: str
    full_name: str
    email: str
    department: Optional[str] = None
    manager: Optional[str] = None


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[str] = None
    department: Optional[str] = None
    manager: Optional[str] = None
    is_active: Optional[bool] = None


class EmployeeResponse(EmployeeBase):
    id: int
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
