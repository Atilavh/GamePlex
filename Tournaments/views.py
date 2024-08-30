from django.shortcuts import render, redirect
from Tournaments.models import Tournament, Upload
from Tournaments.forms import Profile


# Create your views here.

def tournament_list(request):
    tournaments = Tournament.objects.all()

    context = {
        'tournaments': tournaments
    }
    return render(request, 'competitions_list/competitions_list.html', context)


def tournament_image_save(request):
    user = Profile(request.POST, request.FILES)
    if user.is_valid():
        photo = Upload(image=request.FILES['profile'])
        print(photo)
        photo.save()
        return redirect('/home_page/')

    return render(request, 'competitions_list/image.html', {
        'image': user
    })
