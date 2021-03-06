'''
//functions


async def get_rates( from_currency:str, to_currency:str):            -- retruns exchange rate of a currency pair
async def get_income_statement(company_symbol: str):                 -- returns income statement of a company    
async def get_balance_sheet(company_symbol: str):                    -- returns company balance sheet
async def get_cash_flow(company_symbol: str):                        -- returns cash flow of a company
async def get_earnings(company_symbol: str):                         -- returns earning
async def get_company_details( company_symbol: str):                 -- returns company overview details
async def get_listed_companies():                                    -- returns companies listed in the NSE
async def get_delisted_companies():                                  -- returns recently delisted companies in NSE
async def get_earnings_calendar( company_symbol: str):               -- retruns future expected earning calendar of company
async def get_ipo_calendar():                                        -- returns ipo calendar for the next three months of NSE exchange
async def get_inflation_rates():                                     -- returns inflation rates of the country
async def get_real_gdp():                                            -- returns historical gdp
async def get_interest_rates():                                      -- returns interest rate
async def get_unemployment_rate():                                   -- returns historical unemployment rate
'''

from typing import Optional
from app import main


async def get_rates( from_currency:str, to_currency:str):
    return

async def get_income_statement(company_symbol: str):
    return

async def get_balance_sheet(company_symbol: str):
    return

async def get_cash_flow(company_symbol: str):
    return

async def get_earnings(company_symbol: str, from_year: Optional[str]=None , to_year: Optional[str]= None):
    if from_year != None and to_year != None:
        main.cursor.execute(""" SELECT date, value FROM earnings WHERE symbol=%s AND year>=%s AND year<=%s""", ( company_symbol, from_year, to_year, ))
        return main.cursor.fetchall()
    if from_year != None and to_year == None:
        main.cursor.execute(""" SELECT date, value FROM earnings WHERE symbol=%s AND year>=%s """, ( company_symbol, from_year,))
        return main.cursor.fetchall()
    if from_year == None and to_year != None:
        main.cursor.execute(""" SELECT date, value FROM earnings WHERE symbol=%s AND year<=%s """, ( company_symbol, to_year,))
        return main.cursor.fetchall()
    if from_year == None and to_year == None:
        main.cursor.execute(""" SELECT date, value FROM earnings WHERE symbol=%s """, ( company_symbol,))
        return main.cursor.fetchall()
    return

async def get_company_details( company_symbol: str):
    return

async def get_listed_companies():
    return

async def get_delisted_companies():
    return

async def get_earnings_calendar( company_symbol: str):
    return 

async def get_ipo_calendar():
    return

async def get_inflation_rates(from_year: Optional[str]=None , to_year: Optional[str]= None):
    if from_year != None and to_year != None:
        main.cursor.execute(""" SELECT year, rate FROM inflation_rates WHERE year>=%s AND year<=%s""", (from_year, to_year, ))
        return main.cursor.fetchall()
    if from_year != None and to_year == None:
        main.cursor.execute(""" SELECT year, rate FROM inflation_rates WHERE year>=%s """, (from_year,))
        return main.cursor.fetchall()
    if from_year == None and to_year != None:
        main.cursor.execute(""" SELECT year, rate FROM inflation_rates WHERE year<=%s """, (to_year,))
        return main.cursor.fetchall()
    if from_year == None and to_year == None:
        main.cursor.execute(""" SELECT year, rate FROM inflation_rates """)
        return main.cursor.fetchall()



async def get_real_gdp(from_year: Optional[str]=None , to_year: Optional[str]= None):
    if from_year != None and to_year != None:
        main.cursor.execute(""" SELECT year, value FROM gross_domestic_product WHERE year>=%s AND year<=%s""", (from_year, to_year, ))
        return main.cursor.fetchall()
    if from_year != None and to_year == None:
        main.cursor.execute(""" SELECT year, value FROM gross_domestic_product WHERE year>=%s """, (from_year,))
        return main.cursor.fetchall()
    if from_year == None and to_year != None:
        main.cursor.execute(""" SELECT year, value FROM gross_domestic_product WHERE year<=%s """, (to_year,))
        return main.cursor.fetchall()
    if from_year == None and to_year == None:
        main.cursor.execute(""" SELECT year, value FROM gross_domestic_product """)
        return main.cursor.fetchall()


async def get_interest_rates(from_year: Optional[str]=None , to_year: Optional[str]= None):
    if from_year != None and to_year != None:
        main.cursor.execute(""" SELECT year, value FROM interest_rates WHERE year>=%s AND year<=%s""", (from_year, to_year, ))
        return main.cursor.fetchall()
    if from_year != None and to_year == None:
        main.cursor.execute(""" SELECT year, value FROM interest_rates WHERE year>=%s """, (from_year,))
        return main.cursor.fetchall()
    if from_year == None and to_year != None:
        main.cursor.execute(""" SELECT year, value FROM interest_rates WHERE year<=%s """, (to_year,))
        return main.cursor.fetchall()
    if from_year == None and to_year == None:
        main.cursor.execute(""" SELECT year, value FROM interest_rates """)
        return main.cursor.fetchall()


async def get_unemployment_rate(from_year: Optional[str]=None , to_year: Optional[str]= None):
    if from_year != None and to_year != None:
        main.cursor.execute(""" SELECT year, value FROM unemployment_rates WHERE year>=%s AND year<=%s""", (from_year, to_year, ))
        return main.cursor.fetchall()
    if from_year != None and to_year == None:
        main.cursor.execute(""" SELECT year, value FROM unemployment_rates WHERE year>=%s """, (from_year,))
        return main.cursor.fetchall()
    if from_year == None and to_year != None:
        main.cursor.execute(""" SELECT year, value FROM unemployment_rates WHERE year<=%s """, (to_year,))
        return main.cursor.fetchall()
    if from_year == None and to_year == None:
        main.cursor.execute(""" SELECT year, value FROM unemployment_rates """)
        return main.cursor.fetchall()