from datetime import datetime


def to_int( number: str):
    try:
        return int(number)
    except:
        return 


def check_year(year: str):
    try:
        date = datetime( year, "1", "1")
        print(date)
        return date
    except:
        return "null"


