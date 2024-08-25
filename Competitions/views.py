from django.shortcuts import render


# Create your views here.

def competitions_list(request):
    return render(request, 'competitions_list/competitions_list.html')
