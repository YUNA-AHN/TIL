from django.shortcuts import render

# Create your views here.
def calculator(request, num1, num2):
    if num2 == 0:
        condition = False
        divide = 0
    else:
        condition = True
        divide = num1 / num2
    mult = num1 * num2
    minus = num1 - num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'condition' : condition,
        'mult': mult,
        'minus':minus,
        'divide':divide,
    }
    return render(request, 'calculators/calculator.html', context)