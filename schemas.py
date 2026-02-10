# schemas.py
from pydantic import BaseModel
from datetime import datetime

# -------------------------
# User schemas
# -------------------------
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserOut(BaseModel):
    username: str
    email: str
    membership_active: bool

    class Config:
        orm_mode = True  # Required for SQLAlchemy model conversion

# -------------------------
# Reward schemas
# -------------------------
class RewardOut(BaseModel):
    credits: float
    last_updated: datetime

    class Config:
        orm_mode = True

# -------------------------
# Withdrawal schemas
# -------------------------
class WithdrawalRequest(BaseModel):
    amount: float

class WithdrawalOut(BaseModel):
    user_id: int
    amount: float
    status: str
    request_date: datetime

    class Config:
        orm_mode = True
