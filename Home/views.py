from django.shortcuts import render

from accounts_module.models import Registration


# Create your views here.

# Header-Render-Partial-->
def header_component(request):
    profile_wrapper = Registration.objects.filter(is_active=True)
    context = {
        'user': profile_wrapper
    }
    return render(request, 'header_component/header_partial.html', context)


# Home-Page-->
def home_page(request):
    return render(request, 'Base/index.html')


# Footer-Render-Partial-->
def footer_component(request):
    return render(request, 'footer_component/footer_partial.html')
