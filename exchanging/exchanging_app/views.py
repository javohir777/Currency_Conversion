from django.shortcuts import render
import requests

def exchange(request):
    response = requests.get(url="https://api.exchangerate-api.com/v4/latest/USD").json()
    currencies = response.get('rates')

    if request.method == 'GET':
        
        data = {
            'currencies' : currencies
        }

        return render(request, template_name='app/index.html', context=data)
    
    if request.method == 'POST' :
        from_amount = float(request.POST.get('from-amount'))
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount) , 2)

        data  = {
            'currencies' : currencies,
            'from_amount' : from_amount,
            'from_curr' : from_curr,
            'to_curr' : to_curr,
            'converted_amount' : converted_amount
        }
        return render(request, template_name='app/index.html', context=data)
