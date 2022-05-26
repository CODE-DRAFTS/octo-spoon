'''
this file is for routes for fundamental data

//routes
//@router.get("/function=INCOME_STATEMENT")   --to get income statement of a company
//@router.get("/function=BALANCE_SHEET")      --to get balance sheet of a company
//@router.get("/function=CASH_FLOW")          --to get cash flow of a company
//@router.get("/function=EARNINGS")           --to get earning of a company
//@router.get("/function=OVERVIEW")           --to get overview details of a company
//@router.get("/function={LISTING_STATUS}")   --to get listed and delisted companies in the NSE
//@router.get("/function=EARNINGS_CALENDAR")  -- to get expected earning date of a company
//@router.get("/function=IPO_CALENDAR")       --to get nse ipo calendar for next three months
'''


from fastapi import APIRouter


router = APIRouter(
    prefix="/api/v1/fundamentals",
)


@router.get("/function=INCOME_STATEMENT")
async def get_incomestatement( company_symbol: str):
    return {"income statement"}

@router.get("/function=BALANCE_SHEET")
async def get_balancesheet( company_symbol: str):
    return {"balance sheet"}

@router.get("/function=CASH_FLOW")
async def get_cashflow( company_symbol: str):
    return {"cash flow sheet"}

@router.get("/function=EARNINGS")
async def get_earnings( company_symbol: str):
    return {"company earnings sheet"}

@router.get("/function=OVERVIEW")
async def get_companyoverview( company_symbol: str):
    return {"company overview"}

@router.get("/function={LISTING_STATUS}")
async def get_listingstatus(LISTING_STATUS:str , company_symbol: str):
    return {"delisted and listed companies"}

@router.get("/function=EARNINGS_CALENDAR")
async def get_earningcalendar( company_symbol: str):
    return {"company earnings calendar"}

@router.get("/function=IPO_CALENDAR")
async def get_ipocalendar( company_symbol: str):
    return {"3 months IPo calendar"}