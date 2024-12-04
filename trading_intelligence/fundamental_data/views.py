from django.shortcuts import render
import requests
from datetime import datetime
import pytz
import json
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

#@cache_page(3600)
@login_required
def fundamentalData(request):

    # URL de la API de Forex Factory
    url_news = 'https://nfs.faireconomy.media/ff_calendar_thisweek.json'
    response = requests.get(url_news)
    allowed_currencies = ['USD', 'EUR', 'CAD']
    events = []

    if response.status_code == 200:
        all_events = response.json()
        processed_events = []
        dates = [] 

        local_timezone = pytz.timezone('America/Bogota')

        for event in all_events:
            # Filtrar por moneda y por impacto
            if event['country'] in allowed_currencies and event['impact'].lower() != 'low':
                # Convertir a datetime con zona horaria
                date_obj = datetime.fromisoformat(event['date'].replace('Z', '+00:00'))
                # Convertir a hora local
                local_time = date_obj.astimezone(local_timezone)
                event['formatted_date'] = local_time.strftime('%Y-%m-%d')
                event['formatted_time'] = local_time.strftime('%H:%M')
                processed_events.append(event)
                dates.append(local_time)
        
        events = processed_events
        
        if dates:
            min_date = min(dates).strftime('%d/%m/%Y')
            max_date = max(dates).strftime('%d/%m/%Y')
        else:
            min_date = max_date = "No hay datos"

    #configuracion de la API de Alpha Vantage
    url_daily_stock = "https://www.alphavantage.co/query"

    params = {
        "function": "FX_DAILY",
        "from_symbol": "EUR",
        "to_symbol": "USD",
        "apikey": "UEDEPRB4ZY94WOKG",
        "datatype": "json"
    }

    response = requests.get(url_daily_stock, params=params)

    if response.status_code == 200:
        data = response.json()
        daily_data = data['Time Series FX (Daily)']
        
        # Procesar todos los datos históricos
        historical_prices = []
        for date in daily_data:
            historical_prices.append({
                'date': date,
                'open': round(float(daily_data[date]['1. open']), 4),
                'high': round(float(daily_data[date]['2. high']), 4),
                'low': round(float(daily_data[date]['3. low']), 4),
                'close': round(float(daily_data[date]['4. close']), 4)
            })

    #configuracion api de Alpha Vantage market news
    url_news = "https://www.alphavantage.co/query"

    news_params = {
        "function": "NEWS_SENTIMENT",
        "tickers": "FOREX:EUR,FOREX:USD",
        "sort": "LATEST",
        "limit": 4, 
        "apikey": "UEDEPRB4ZY94WOKG"
    }

    news_response = requests.get(url_news, params=news_params)
    news_data = []

    if news_response.status_code == 200:
        news_json = news_response.json()
        print("API URL:", news_response.url)  # Debug URL
        
        if 'feed' in news_json:
            print(f"Found {len(news_json['feed'])} news items")
            for item in news_json['feed'][:4]:
                news_data.append({
                    'title': item.get('title', ''), 
                    'summary': item.get('summary', ''),
                    'source': item.get('source', ''),
                    'url': item.get('url', ''),
                    'time_published': item.get('time_published', '')
                })
    
        print(f"Processed {len(news_data)} news items")
        
    return render(request, 'fundamental_data.html', {
        'events': events,
        'min_date': min_date,
        'max_date': max_date,
        'historical_prices': json.dumps(historical_prices),  # Serialize to JSON
        'news_data': news_data
    })
