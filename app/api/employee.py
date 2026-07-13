from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.crud.employee import (
    create_employee,
    delete_employee,
    get_all_employees,
    get_employee,
    update_employee,
)
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeResponse,
    EmployeeUpdate,
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)


@router.post("/", response_model=EmployeeResponse)
def create(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db, employee)


@router.get("/", response_model=List[EmployeeResponse])
def get_all(db: Session = Depends(get_db)):
    return get_all_employees(db)


@router.get("/{employee_id}", response_model=EmployeeResponse)
def get(employee_id: int, db: Session = Depends(get_db)):
    employee = get_employee(db, employee_id)

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


@router.put("/{employee_id}", response_model=EmployeeResponse)
def update(
    employee_id: int,
    employee: EmployeeUpdate,
    db: Session = Depends(get_db),
):
    updated_employee = update_employee(db, employee_id, employee)

    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return updated_employee


@router.delete("/{employee_id}")
def delete(employee_id: int, db: Session = Depends(get_db)):
    deleted_employee = delete_employee(db, employee_id)

    if not deleted_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return {"message": "Employee deleted successfully"}
