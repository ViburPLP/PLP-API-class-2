import requests
from django.shortcuts import render
from django.http import HttpResponse

def dashboard (request):
    response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=ZROA09JARY1NMF05')
    stock_data = response.json()
    result = stock_data['Time Series (Daily)']



    if 'Time Series (Daily)' in stock_data:
        stock_prices = []
        for date, value in stock_data['Time Series (Daily)'].items():
            stock_price = Stockprice.objects.create(
                date=date,
                stock_symbol='AAPL',
                price = value['4. close'],
            )

    return render(request, 'dashboard.html' , {'result': result})

