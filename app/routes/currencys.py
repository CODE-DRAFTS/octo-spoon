'''

//routes
//@router.get('/function=CURRENCY_EXCHANGE_RATE')         --returns the exchange rate of a currency pair


'''
from fastapi import APIRouter



router = APIRouter(
    prefix="/api/v1/currencies",
)


@router.get('/function=CURRENCY_EXCHANGE_RATE')
async def get_exchange_rate(to_currency: str):
    return {"exchange rates endpoint"}

