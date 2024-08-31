from django.shortcuts import render, redirect
from Tournaments.models import Tournament
from Tournaments.forms import Profile


# Create your views here.

def tournament_list(request):
    tournaments = Tournament.objects.filter(is_active=True)
    context = {
        'tournaments': tournaments
    }
    return render(request, 'competitions_list/competitions_list.html', context)


def tournament_image_save(request):
    image_of_tournament = Profile()
    if request.method == 'POST':
        image_of_tournament = Profile(request.POST, request.FILES)
        if image_of_tournament.is_valid():
            image = Tournament(image=request.FILES["Image"])
            image.save()
            return redirect('upload')
    return render(request, 'competitions_list/image.html', {
        'upload': image_of_tournament
    })
