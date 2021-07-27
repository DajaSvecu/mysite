from django.shortcuts import render
from django.views import generic

from .models import Counter

# Create your views here.

class MainView(generic.ListView):
    model = Counter
    template_name = 'main_page/main.html'
    def get(self, request, *args, **kwargs):
        c = Counter.objects.get(pk=1)
        c.counter += 1
        c.save()
        return render(request, self.template_name, {'pocet_navstev':c})