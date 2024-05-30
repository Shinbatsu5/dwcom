from django.shortcuts import render
from.models import Articles
from django.views.generic import ListView

def home(request):
    home = Articles.objects.order_by ('-date')
    return render(request,'main/index.html',{'home': home})


class pagination6 (ListView):
    paginate_by = 4
    model = Articles
    template_name = 'main/index.html'
    context_object_name = 'article'
    extra_context = {'title': 'Новости'}

def about(request):
    return render(request,'main/about.html')

def contacts(request):
    return render(request,'main/contacts.html')

def injsystem(request):
    return render(request,'main/injsystem.html')

def licenses(request):
    return render(request,'main/licenses.html')

def projectsupplies(request):
    return render(request,'main/projectsupplies.html')

def requisites(request):
    return render(request,'main/requisites.html')

def vakansii(request):
    return render(request,'main/vakansii.html')

def news(request):
    return render(request,'news/news.html')

def realise(request):
    return render(request,'realise/realise.html')

def partners(request):
    return render(request,'partners/partners.html')
