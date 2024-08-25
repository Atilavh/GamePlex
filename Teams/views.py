from django.shortcuts import render


# Create your views here.

def team_list(request):
    return render(request, 'team_list/team_list.html')
