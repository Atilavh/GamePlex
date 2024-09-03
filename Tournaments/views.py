from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from Tournaments.models import Tournament
from Tournaments.forms import Profile
from jalali_date import datetime2jalali, date2jalali


# Create your views here.

def tournament_list(request):
    tournaments = Tournament.objects.filter(is_active=True)
    # solar_date = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')
    context = {
        'tournaments': tournaments,
        # 'date': solar_date
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


def paging(request):
    query = Tournament.objects.all()
    page = Paginator(query, 1)
    req = request.GET.get('page')
    page_obj = page.get_page(req)
    return render(request, 'competitions_list/competitions_list.html', {'page_obj': page_obj})
