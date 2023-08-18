from django.shortcuts import render

# Create your views here.




def index(request):
    context={}
    return render(request, 'web/index.html', context)

def protfolio_nayel(request):
    context={}
    return render(request, 'web/protfolio-nayel.html', context)