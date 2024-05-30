from django.shortcuts import render
from.models import Realise
from django.views.generic import DetailView ,ListView


def realise(request):
    realise = Realise.objects.order_by('-date')
    return render(request,'realise/realise.html',{'realise': realise})



class realisedetailview (DetailView):
    model = Realise
    template_name = 'realise/detail_view.html'
    context_object_name = 'realise'

class pagination4 (ListView):
    paginate_by = 4
    model = Realise
    template_name = 'realise/realise.html'
    context_object_name = 'realise'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context