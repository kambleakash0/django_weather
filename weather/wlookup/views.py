import os
from datetime import tzinfo
from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests
    from django.template.defaulttags import register
    from datetime import datetime
    import pytz

    @register.filter
    def dt(timestamp):
        date = datetime.fromtimestamp(int(timestamp), pytz.timezone('ASIA/Kolkata')).strftime('%d-%m-%Y')
        return date

    @register.filter
    def tm(timestamp):
        time = datetime.fromtimestamp(int(timestamp), pytz.timezone('ASIA/Kolkata')).strftime('%H:%M:%S')
        return time

    api_key = os.environ['OPENWEATHER_API_KEY']

    if request.method == "POST":
        lon = request.POST['lon']
        lat = request.POST['lat']
        
        url = "http://api.openweathermap.org/data/2.5/air_pollution?lat={}&lon={}&appid={}".format(lat, lon, api_key)
        api_rq = requests.get(url)
        try:
            response = api_rq.json() # json.loads(api_rq.content)
        except Exception as e:
            response = "Error: {}".format(e)
        if response and 'Error' not in response:
            if response['list'][0]['main']['aqi'] == 1:
                aqi_color = 'good'
            elif response['list'][0]['main']['aqi'] == 2:
                aqi_color = 'fair'
            elif response['list'][0]['main']['aqi'] == 3:
                aqi_color = 'moderate'
            elif response['list'][0]['main']['aqi'] == 4:
                aqi_color = 'poor'
            else:
                aqi_color = 'verypoor'
        return render(request, 'home.html', {'response': response, 'aqi_color': aqi_color})
    
    else:
        url = "http://api.openweathermap.org/data/2.5/air_pollution?lat=28.7041&lon=77.1025&appid={}".format(api_key)
        api_rq = requests.get(url)
        try:
            response = api_rq.json() # json.loads(api_rq.content)
        except Exception as e:
            response = "Error: {}".format(e)
        if response and 'Error' not in response:
            if response['list'][0]['main']['aqi'] == 1:
                aqi_color = 'good'
            elif response['list'][0]['main']['aqi'] == 2:
                aqi_color = 'fair'
            elif response['list'][0]['main']['aqi'] == 3:
                aqi_color = 'moderate'
            elif response['list'][0]['main']['aqi'] == 4:
                aqi_color = 'poor'
            else:
                aqi_color = 'verypoor'
        return render(request, 'home.html', {'response': response, 'aqi_color': aqi_color})

def about(request):
    return render(request, 'about.html', {})