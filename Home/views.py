from django.shortcuts import render


# Create your views here.

# Header-Render-Partial-->
def header_component(request):
    return render(request, 'header_component/header_partial.html')


# Home-Page-->
def home_page(request):
    return render(request, 'Base/index.html')


# Footer-Render-Partial-->
def footer_component(request):
    return render(request, 'footer_component/footer_partial.html')

# def pageing(request):
#     query = Registration.objects.all()
#     page = Paginator(query, 3)
#     req = request.GET.get('page', 1)
#     page_obj = page.page(req)
#     context = {
#         'page_obj': page_obj,
#     }
#     return render(request, '', context)
