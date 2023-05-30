from django.shortcuts import render

# Create your views here.

def abd(request):
    d={'age': 20}
    return render(request,'abd.html',context=d)
