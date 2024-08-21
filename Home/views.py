from django.shortcuts import render


# Create your views here.


def header_component(request):
    return render(request, 'header_component/header_partial.html')


def footer_component(request):
    return render(request, 'footer_component/footer_partial.html')
