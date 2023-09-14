from django.shortcuts import render

# Create your views here.
def calculators(request):
    return render(request, 'calculators/calculators.html')

# def result(request):
#     print(request) # calculators
#     print(type(request)) # <class 'django.core.handlers.wsgi.WSGIRequest'>
#     print(dir(request)) # ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', ...]
#     print(request.GET) # <QueryDict: {'num1': ['dd'], 'num2': ['ddd']}>
#     print(request.GET.get('num1'))
#     print(request.GET.get('num2'))

def result(request):
    num1 = request.GET.get('num1')
    num2 = request.GET.get('num2')
    context = {
        'num1' : num1,
        'num2' : num2,
    }
    return render(request, 'calculators/result.html', context)