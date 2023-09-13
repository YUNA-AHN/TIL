from django.shortcuts import render

# Create your views here.
def calculators(request):
    return render(request, 'calculators/calculators.html')

def result(request):
    print(request) # calculators
    print(type(request)) # <class 'django.core.handlers.wsgi.WSGIRequest'>
    print(dir(request)) # ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', ...]
    print(request.GET) # <QueryDict: {}>
    print(request.GET.get('message'))