from django.shortcuts import render
from.models import Articles
from django.views.generic import DetailView ,ListView

def news(request):
    news = Articles.objects.order_by('-date')
    return render(request,'news/news.html',{'news': news})


class newsdetailview (DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

class pagination (ListView):
    paginate_by = 4
    model = Articles
    template_name = 'news/news.html'
    context_object_name = 'article'
    extra_context = {'title': 'Новости'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context