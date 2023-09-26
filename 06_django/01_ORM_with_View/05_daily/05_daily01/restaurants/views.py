from django.shortcuts import render, get_list_or_404, redirect
from .models import Restaurant
from .forms import RestaurantForm

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants' : restaurants,
    }
    return render(request, 'restaurants/index.html', context)

def new(request):
    form = RestaurantForm()
    context = {
        'form':form,
    }
    return render(request, 'restaurants/new.html', context)

def create(request):
    form = RestaurantForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('restaurants:index') 
    context = {
        'form':form,
    }
    return render(request, 'restaurants/new.html', context)

    # name = request.POST.get('name')
    # desciption = request.POST.get('desciption')
    # address = request.POST.get('address')
    # phone_number = request.POST.get('phone_number')
    
    # restaurant = Restaurant(name=name, desciption=desciption,
    #                         address=address, phone_number=phone_number)
    # restaurant.save()
    # return redirect('articles:index')
    
def detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    context = {
        'restaurant':restaurant,
    }
    return render(request, 'restaurants/detail.html', context)