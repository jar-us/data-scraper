from nsepy import get_history

from datetime import date, datetime

def get_historical_data(indexName, startDate, endDate):
    nifty_next50 = get_history(symbol=indexName,
                               start=date(getDate(startDate).year, getDate(startDate).month, getDate(startDate).day),
                               end=date(getDate(endDate).year, getDate(endDate).month, getDate(endDate).day),
                               index=True)
    print(nifty_next50)
    

def getDate(startDate, format='%Y-%m-%d'):
    date = datetime.strptime(startDate, format)
    return date