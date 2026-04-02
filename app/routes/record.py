from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.record import Record
from app.schemas.record import RecordCreate, RecordResponse

router = APIRouter(prefix="/records", tags=["Records"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Record
from fastapi import Header

@router.post("/", response_model=RecordResponse)
def create_record(
    record: RecordCreate,
    role: str = Header(None),
    db: Session = Depends(get_db)
):
    
    if role != "admin":
        raise HTTPException(status_code=403, detail="Only admin can create records")

    if record.type not in ["income", "expense"]:
        raise HTTPException(status_code=400, detail="Type must be income or expense")

    db_record = Record(**record.dict(), user_id=1)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

# Get All Records
from fastapi import Query

@router.get("/", response_model=list[RecordResponse])
def get_records(
    type: str = Query(None),
    category: str = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Record)

    if type:
        query = query.filter(Record.type == type)

    if category:
        query = query.filter(Record.category == category)

    return query.all()

@router.put("/{record_id}", response_model=RecordResponse)
def update_record(record_id: int, updated: RecordCreate, db: Session = Depends(get_db)):
    record = db.query(Record).filter(Record.id == record_id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    for key, value in updated.dict().items():
        setattr(record, key, value)

    db.commit()
    db.refresh(record)
    return record

@router.delete("/{record_id}")
def delete_record(record_id: int, db: Session = Depends(get_db)):
    record = db.query(Record).filter(Record.id == record_id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    db.delete(record)
    db.commit()

    return {"message": "Record deleted successfully"}