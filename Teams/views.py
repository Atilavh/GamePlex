from django.shortcuts import render
from .models import Team


# Create your views here.

def team_list(request):
    queryset = Team.objects.all()
    context = {
        'Team': queryset
    }
    return render(request, 'team_list/team_list.html', context)
