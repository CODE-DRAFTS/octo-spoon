from datetime import datetime
from fastapi import HTTPException, status


def to_int( number: str):
    try:
        return int(number)
    except:
        return 



def validate_year(year: str):
    return

def check_year(from_year: str, to_year: str):
    if from_year!= None or to_year!= None:
        if from_year != None:
            if to_int(from_year) == None:
                raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"from_year={from_year} is not a valid year")
        if to_year != None:
            if  to_int(to_year) == None:
                raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail=f"to_year={to_year} is not a valid year")


