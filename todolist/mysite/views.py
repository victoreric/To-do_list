from django.shortcuts import render
import requests
import json
from datetime import datetime, timedelta

def index(request):
    url = "https://api.covid19api.com/summary"
    # A summary of new and total cases per country updated daily.
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)

    data=response.json()
    datanegara = data['Countries']
    rus=datanegara[140]
    case2 = []
    result2 = {}
    result2['Country'] = rus['Country']
    result2['CountryCode'] = rus['CountryCode']
    result2['NewConfirmed'] = rus['NewConfirmed']
    result2['TotalConfirmed'] = rus['TotalConfirmed']
    result2['NewDeaths'] = rus['NewDeaths']
    result2['TotalDeaths'] = rus['TotalDeaths']
    result2['NewRecovered'] = rus['NewRecovered']
    result2['NewTotalRecoveredConfirmed'] = rus['TotalRecovered']
    result2['Date'] = rus['Date']
    case2.append(result2)

    update = datetime.now()-timedelta(days=1)

    context = {
        'Title' : 'Home',
        'case2' : case2,
        'update' : update,
    }
    return render(request,'index.html', context)