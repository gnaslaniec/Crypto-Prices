from django.shortcuts import render
import requests
import json

def home(request):
    # Noticias
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    # Preços
    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,ETC,LTC,XRP,EOS,BCH,NEO,USDT,ZEC,ADA,MIOTA&tsyms=BRL,USD")
    price = json.loads(price_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})
    
def prices(request):
    if request.method == 'POST':
        quote = request.POST['quote']
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=BRL,USD".format(quote.upper()))
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto}) 
    else:
        notfound = "Insira o simbolo de uma cryptomoeda: "
        return render(request, 'prices.html', {'notefound': notfound}) 
    
    