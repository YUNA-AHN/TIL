from django.shortcuts import render

product_price = {"라면":980,"홈런볼":1500,"칙촉":2300, "식빵":1800}

# Create your views here.
def price(request, thing, cnt):
    if product_price.get(thing):
        total = product_price[thing] * cnt
    else:
        total = None
        
    context = {
        'thing': thing,
        'cnt' : cnt,
        'total' : total,
    }
    return render(request, 'prices/price.html', context)