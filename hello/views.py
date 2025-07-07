from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect


def index(request):
    headers = {
        'accept': '*/*',
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Referer': 'habr.com'
        }
    URL = 'https://yandex.ru/maps/213/moscow/stops/stop__9646632/?ll=37.735570%2C55.684708&tab=overview&z=19'
    req = requests.get(URL, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, 'lxml')
    all_products_hrefs = soup.find(class_='masstransit-prognoses-view__title-text').text
    
    from datetime import datetime
    current_datetime = str(datetime.now())
    b=current_datetime.split("-")
    c=b[0]
    d=b[1]
    e=b[2].split(" ")
    f=e[0]
    g=e[1]
    kl=g.split(".")
    io=kl[0]
    ty=io.replace(io[:2],str(int(io[:2])+3))
    date_new256=f+'.'+d+'.'+c+'  '+ty



    data = {"header": all_products_hrefs,"date":date_new256}
    return render(request, "index.html", context=data)