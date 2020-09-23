from django.shortcuts import render



# Create your views here.

def post_list(request):
    return render(request, 'blog/landing_page.html', {})

def landing(request):
    return render(request, 'blog/landing_page.html', {})


