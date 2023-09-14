from django.shortcuts import render

# Create your views here.
def certification1(reqest):
    age = range(25,31)
    grade = ['a','b','c','s']
    context = {
        'age': age,
        'grade': grade,
    }
    return render(reqest, 'certifications/certification1.html', context)

def certification2(reqest):
    age = range(25,31)
    grade = ['a','b','c','s']
    context = {
        'age': age,
        'grade': grade,
    }
    return render(reqest, 'certifications/certification2.html', context)

def certification3(reqest):
    age = range(25,31)
    grade = ['a','b','c','s']
    context = {
        'age': age,
        'grade': grade,
    }
    return render(reqest, 'certifications/certification3.html', context)