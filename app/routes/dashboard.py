from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.record import Record

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/summary")
def get_summary(db: Session = Depends(get_db)):
    
    records = db.query(Record).all()

    total_income = sum(r.amount for r in records if r.type == "income")
    total_expense = sum(r.amount for r in records if r.type == "expense")

    net_balance = total_income - total_expense

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "net_balance": net_balance
    }
@router.get("/category-summary")
def category_summary(db: Session = Depends(get_db)):
    
    records = db.query(Record).all()

    result = {}

    for r in records:
        if r.category not in result:
            result[r.category] = 0
        result[r.category] += r.amount

    return result