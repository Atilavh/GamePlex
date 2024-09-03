from django.shortcuts import render
from Tournaments.models import Tournament
from accounts_module.models import User


# Create your views here.

# Header-Render-Partial-->
def header_component(request):
    return render(request, 'header_component/header_partial.html')


# Home-Page-->
def home_page(request):
    user_query = User.objects.filter(is_active=True)
    query = Tournament.objects.filter(is_active=True)
    context = {
        'obj': query,
        'users': user_query,
    }
    return render(request, 'Base/index.html', context)


# Footer-Render-Partial-->
def footer_component(request):
    return render(request, 'footer_component/footer_partial.html')
