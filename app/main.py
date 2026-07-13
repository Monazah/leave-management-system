from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.api.health import router as health_router
from app.api.employee import router as employee_router

from app.database.connection import get_db
from app.models.employee import Employee

app = FastAPI(
    title="Leave Management System",
    version="1.0.0",
)

# Static Files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

# API Routers
app.include_router(health_router)
app.include_router(employee_router)


@app.get("/")
def dashboard(request: Request, db: Session = Depends(get_db)):

    total_employees = db.query(Employee).count()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "total_employees": total_employees,
        },
    )


@app.get("/employees")
def employees(request: Request, db: Session = Depends(get_db)):

    employees = db.query(Employee).all()

    return templates.TemplateResponse(
        "employees.html",
        {
            "request": request,
            "employees": employees,
        },
    )
