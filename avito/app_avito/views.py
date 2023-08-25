from django.shortcuts import render, reverse, redirect
from .models import Avito
from .forms import AvitoForms

def index(request):

    avitos = Avito.objects.all()
    context = {"avitos": avitos}
    return render(request, "index.html", context=context)

def top_sellers(request):
    return render(request, "top-sellers.html")

def post_advertisement(request):
    if request.method == "POST":
        form = AvitoForms(request.POST, request.FILES)
        if form.is_valid():
            avito = Avito(**form.cleaned_data)
            avito.user = request.user
            avito.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AvitoForms()
    context = {"form": form}
    return render(request, "advertisement-post.html", context=context)
