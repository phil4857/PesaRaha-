# models.py
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime
from .database import Base  # ✅ relative import for Render
from datetime import datetime

# -------------------------
# User table
# -------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    membership_active = Column(Boolean, default=False)
    membership_fee_paid = Column(Float, default=0)

# -------------------------
# Rewards table
# -------------------------
class Reward(Base):
    __tablename__ = "rewards"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    credits = Column(Float, default=0)
    last_updated = Column(DateTime, default=datetime.utcnow)

# -------------------------
# Referrals table
# -------------------------
class Referral(Base):
    __tablename__ = "referrals"

    id = Column(Integer, primary_key=True)
    referrer_id = Column(Integer, nullable=False)
    referee_id = Column(Integer, nullable=False)
    bonus_credits = Column(Float, default=0)

# -------------------------
# Withdrawals table
# -------------------------
class Withdrawal(Base):
    __tablename__ = "withdrawals"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(String, default="PENDING")  # PENDING / APPROVED / REJECTED
    request_date = Column(DateTime, default=datetime.utcnow)
