import requests
from django.shortcuts import render
from django.http import HttpResponse
# from.models import Stockprice

def dashboard (request):
    response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=ZROA09JARY1NMF05')
    stock_data = response.json()
    result = stock_data['Time Series (Daily)']

    dates = []
    prices = []
    for date, values in result.items():
        dates.append(date)
        prices.append(float(values["4. close"]))

    return render(request, 'dashboard.html' , {'dates': dates, 'prices': prices})

