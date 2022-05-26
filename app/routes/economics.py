'''
this file will have routes for getting economic indicators data

//routes
//router.get('/?function=INFLATION_RATES')  --to get inflation rates
//@router.get('/function=REAL_GDP')         --to get real gross domestic product
//@router.get('/function=INTEREST_RATE')    --to get interst rate
//@router.get('/function=UNEMPLOYMENT')     --to get unemployement rates

'''
from fastapi import APIRouter
from typing import Optional
from app import utils


router = APIRouter(
    prefix="/api/v1/economics"
)


@router.get('/function=INFLATION_RATES')
async def get_inflationrates(from_year: Optional[str]= None, to_year:Optional[str] = None):
    return {"inflation rates"}

@router.get('/function=REAL_GDP')
async def get_gdp(from_year: Optional[str]= None, to_year:Optional[str] = None):
    return("real gdp")


@router.get('/function=INTEREST_RATE')
async def get_interestrate(from_year: Optional[str]= None, to_year:Optional[str] = None):
    return("interest rate")


@router.get('/function=UNEMPLOYMENT')
async def get_unemploymentrate(from_year: Optional[str]= None, to_year:Optional[str] = None):
    return("consumer price index")

