
from fastapi import FastAPI,Depends
from schema.user import UserCreate
from model.user import SessionLocal,Base,engine
from sqlalchemy.orm import Session

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.post('/usr/signup')
async def Sign_Up(user:UserCreate, db:Session = Depends(get_db)):
    new_user = user(Firstname = user.FirstName, LastName = user.LastName, Email = user.Email, Password = user.Password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
