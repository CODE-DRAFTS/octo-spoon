'''
this file will have routes for getting economic indicators data

//routes
//router.get('/?function=INFLATION_RATES')  --to get inflation rates
//@router.get('/function=REAL_GDP')         --to get real gross domestic product
//@router.get('/function=INTEREST_RATE')    --to get interst rate
//@router.get('/function=UNEMPLOYMENT')     --to get unemployement rates

'''
from fastapi import APIRouter, HTTPException, status
from typing import Optional
from app import utils
from app.database import fetchs, deletes, inserts


router = APIRouter(
    prefix="/api/v1/economics"
)


@router.get('/function=INFLATION_RATES')
async def get_inflationrates(from_year: Optional[str]= None, to_year:Optional[str] = None):
    if from_year!= None or to_year!= None:
        if from_year != None:
            if utils.to_int(from_year) == None:
                print(utils.to_int(from_year))
                print("a")
                raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"from_year={from_year} is not a valid year")
        if to_year != None:
            if  utils.to_int(to_year) == None:
                print(utils.to_int(to_year))
                raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"to_year={to_year} is not a valid year")
    #TODO: validate year inputs
    return await fetchs.get_inflation_rates(from_year, to_year)


@router.get('/function=REAL_GDP')
async def get_gdp(from_year: Optional[str]= None, to_year:Optional[str] = None):
    return("real gdp")


@router.get('/function=INTEREST_RATE')
async def get_interestrate(from_year: Optional[str]= None, to_year:Optional[str] = None):
    return("interest rate")


@router.get('/function=UNEMPLOYMENT')
async def get_unemploymentrate(from_year: Optional[str]= None, to_year:Optional[str] = None):
    return("consumer price index")

