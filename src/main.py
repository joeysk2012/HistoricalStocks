
import lxml 
import html 
import requests
import json
import datetime
from dateutil.relativedelta import relativedelta


#validate date text format
def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    

#operate function for each tracker. 
def operate(tracker):    
    
    jsonData=Share(tracker).get_historical(start, end) #52 week low
    pricearr= list(range(len(jsonData)))
    for i in range(0, len(jsonData)):
        pricearr[i]=jsonData[i]['Low']#gets array of low values
        
    name=Share(tracker).get_name()#get company name
    price=jsonData[0]['Close']#get historical close price
    low=min(list(map(float,pricearr)))
    currentPrice=Share(tracker).get_price()#get current price
    profit=((float(currentPrice)-float(price))/float(price))*100
    perlow=(float(price)/float(low)-1)*100
    if perlow<=10 and profit>=12:
           print(jsonData[0]['Symbol'])
           print("company", name)
           print("historical price is", price)
           print("historical 52 week low is", low)
           print("the historical percent of low is", "{0:.2f}".format(perlow),"%")
           print("current price is", currentPrice)
           print("your percent return is", "{0:.2f}".format(profit))
    

#this is the main portion of the code.    
from yahoo_finance import Share
d=input('input a date in yyyy-MM-dd format to check historical prices')
validate(d)
start=""
#strips down the time to yyy-mm-dd
def __datetime(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d')
end=__datetime(d)
start=end-relativedelta(years=1)
start=start.strftime('%Y-%m-%d')
end=end.strftime('%Y-%m-%d')


indust=input('What industry do you want to look up?: All (A), Consumer Discretionary (D) Consumer Staples (S), Energy (E) Financial (F), Healthcare (H) Industrial (I), Real Estate (R) Info. Tech. (T), Utilities (U)' )
with open('SPALL.txt', 'r') as f:
    trackers = [line.strip() for line in f]
for i in range(0,len(trackers)):
    operate(trackers[i])
    #jsonData=Share(trackers[i]).get_historical(d, d)
    #jsonToPython =json.loads(jsonData)
    #print(jsonData[0]['Symbol'])
    

