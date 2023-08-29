from django.shortcuts import render, reverse, redirect
from .models import Avito
from .forms import AvitoForm
from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()

def index(request):

    title = request.GET.get('query')
    if title:
        avitos = Avito.objects.filter(title__iexact=title)
    else:
        avitos = Avito.objects.all()
    context = {
        "avitos": avitos
    }

    return render(request, "app_avito/index.html", context=context)

def top_sellers(request):
    users = User.objects.annotate(
        adv_count=Count("avito")
    ).order_by('-adv_count')

    context = {
        "users": users
    }
    return render(request, "app_avito/top-sellers.html", context=context)

def post_advertisement(request):
    if request.method == "POST":
        form = AvitoForm(request.POST, request.FILES)
        if form.is_valid():
            avito = form.save(commit=False)
            avito.user = request.user
            avito.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AvitoForm()
    context = {
        "form": form
    }
    return render(request, "app_avito/advertisement-post.html", context=context)

def advertisement_view(request, pk):
    advertisement = Avito.objects.get(pk=pk)
    context = {
        "advertisement": advertisement
    }
    return render(request, "app_avito/advertisement.html", context)


