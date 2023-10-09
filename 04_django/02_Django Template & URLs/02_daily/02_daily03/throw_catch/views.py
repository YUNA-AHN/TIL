from django.shortcuts import render

# Create your views here.
def first(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'throw_catch/first.html', context)


def second(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'throw_catch/second.html', context)