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

    response2= requests.get("https://api.apify.com/v2/key-value-stores/1brJ0NLbQaJKPTWMO/records/LATEST?disableRedirect=true")

    datarusia= response2.json()
    infectedByRegion=(datarusia['infectedByRegion'])
    tomsk = (infectedByRegion[32])
    case3 = []
    result3 = {}
    result3['region'] = tomsk['region']
    result3['isoCode'] = tomsk['isoCode']
    result3['infected'] = tomsk['infected']
    result3['recovered'] = tomsk['recovered']
    result3['deceased'] = tomsk['deceased']
    case3.append(result3)  

    case4 =[]
    for reg in infectedByRegion:
        result4={}
        result4['region'] = reg['region']
        result4['infected'] = reg['infected']
        result4['recovered'] = reg['recovered'] 
        result4['deceased'] = reg['deceased']
        case4.append(result4)


    context = {
        'Title' : 'Home',
        'case2' : case2,
        'case3' : case3,
        'case4': case4,
        'update' : update,
    }
    return render(request,'index.html', context)