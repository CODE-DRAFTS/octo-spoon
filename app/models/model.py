from pydantic import BaseModel, EmailStr
from typing import Optional


class NewUser(BaseModel):
    email: EmailStr
    passowrd: str
    name: str
    phone: str
    role: str

class UpdateUser(BaseModel):
    email: Optional[EmailStr] 
    passowrd: Optional[str]
    name: Optional[str]
    phone: Optional[str]
    role: Optional[str]

class News(BaseModel):
    title: str
    content: str 
    category: str 

class UodateNews(BaseModel):
    title: Optional[str]
    content: Optional[str] 
    category: Optional[str]


class ExchangeRate(BaseModel):
    currency: str
    rate: float

class IncomeStatement(BaseModel):
    pass

class BalanceSheet(BaseModel):
    pass

class CashFlow(BaseModel):
    pass

class Company(BaseModel):
    pass

class Earnings(BaseModel):
    pass

