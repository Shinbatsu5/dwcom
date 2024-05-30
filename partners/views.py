from django.shortcuts import render
from.models import Partners,Categories
from django.views.generic import DetailView ,ListView

def partners(request):
    partners = Partners.objects.all()
    category = Categories.objects.all()
    return render(request,'partners/partners.html',{'partners': partners,'category':category})


class partnersdetailview (DetailView):
    model = Partners
    template_name = 'partners/detail_view.html'
    context_object_name = 'partners'

class pagination5 (ListView):
    paginate_by = 4;
    model = Partners
    template_name = 'partners/partners.html'
    context_object_name = 'partners'

    def get_context_data(self, **kwargs):
        context = super(pagination5, self).get_context_data(**kwargs)
        context['category'] = Categories.objects.all()
        if sort := self.request.GET.get('sort'):
            Partners.order_by(*sort.split(','))
        return context