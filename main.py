from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import crud, schemas, models

Base.metadata.create_all(bind=engine)
app = FastAPI(title="PeSaRaha🤑💰💲 API")

@app.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email exists")
    return crud.create_user(db, user.username, user.email, user.password)

@app.post("/pay-membership/{user_id}", response_model=schemas.UserOut)
def pay_membership(user_id: int, db: Session = Depends(get_db)):
    return crud.pay_membership(db, user_id)

@app.get("/rewards/{user_id}", response_model=schemas.RewardOut)
def get_reward(user_id: int, db: Session = Depends(get_db)):
    reward = db.query(models.Reward).filter(models.Reward.user_id==user_id).first()
    if not reward:
        return crud.add_reward(db, user_id, 0)
    return reward

@app.post("/withdrawals/{user_id}", response_model=schemas.WithdrawalOut)
def request_withdrawal(user_id: int, req: schemas.WithdrawalRequest, db: Session = Depends(get_db)):
    return crud.request_withdrawal(db, user_id, req.amount)

@app.post("/admin/approve/{withdrawal_id}")
def approve(withdrawal_id: int, db: Session = Depends(get_db)):
    return crud.approve_withdrawal(db, withdrawal_id)

@app.post("/admin/reject/{withdrawal_id}")
def reject(withdrawal_id: int, db: Session = Depends(get_db)):
    return crud.reject_withdrawal(db, withdrawal_id)
