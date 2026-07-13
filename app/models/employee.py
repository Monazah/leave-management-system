from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database.base import Base


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)

    employee_id = Column(String(20), unique=True, nullable=False)

    username = Column(String(100), unique=True, nullable=False)

    full_name = Column(String(150), nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    department = Column(String(100))

    manager = Column(String(100))

    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
