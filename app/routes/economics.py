'''
this file will have routes for getting economic indicators data

//routes
//router.get('/?function=INFLATION_RATES')  --to get inflation rates
//@router.get('/function=REAL_GDP')         --to get real gross domestic product
//@router.get('/function=INTEREST_RATE')    --to get interest rate
//@router.get('/function=UNEMPLOYMENT')     --to get unemployement rates
'''

from fastapi import APIRouter, HTTPException, status
from typing import Optional
from app import utils
from app.database import fetchs


router = APIRouter(
    prefix="/api/v1/economics",
    tags=["ECONOMIC INDICATORS"]
)


@router.get('/function=INFLATION_RATES')
async def get_inflationrates(from_year: Optional[str]= None, to_year:Optional[str] = None):
    utils.check_year(from_year, to_year)
    #TODO: validate year inputs
    return await fetchs.get_inflation_rates(from_year, to_year)


@router.get('/function=REAL_GDP')
async def get_gdp(from_year: Optional[str]= None, to_year:Optional[str] = None):
    utils.check_year(from_year, to_year)
    #TODO: validate year inputs
    return await fetchs.get_real_gdp(from_year, to_year)


@router.get('/function=INTEREST_RATE')
async def get_interestrate(from_year: Optional[str]= None, to_year:Optional[str] = None):
    utils.check_year(from_year, to_year)
    return await fetchs.get_interest_rates(from_year, to_year)


@router.get('/function=UNEMPLOYMENT')
async def get_unemploymentrate(from_year: Optional[str]= None, to_year:Optional[str] = None):
    utils.check_year(from_year, to_year)
    #TODO: validate year inputs
    return await fetchs.get_unemployment_rate(from_year, to_year)

