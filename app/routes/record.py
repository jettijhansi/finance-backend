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
@router.post("/", response_model=RecordResponse)
def create_record(record: RecordCreate, db: Session = Depends(get_db)):
    
    if record.type not in ["income", "expense"]:
        raise HTTPException(status_code=400, detail="Type must be income or expense")

    db_record = Record(**record.dict(), user_id=1)  # temporary user
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