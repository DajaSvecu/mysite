from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError
from django.views import generic
from .models import User


# Create your views here.
# Slouzi pro zobrazeni stranky uzivateli

class MainView(generic.ListView):
    model = User
    template_name = 'main.html'

class HlavniView(generic.ListView):
    model = User
    template_name = 'todo/hlavni.html'
    context_object_name = 'list_uzivatelu'

class TodoView(generic.DetailView):
    model = User
    template_name = 'todo/detail.html'

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        if request.POST['newitem'] == '':
            msg = 'Napsal jsi prazdny ukol!'
            return render(request, self.template_name, {'user': user, 'error_msg':msg})
        user.todoitems_set.create(item=request.POST['newitem'], date=timezone.now())
        user.save()
        return render(request, self.template_name, {'user': user})

class FinishedView(generic.DetailView):
    model = User
    
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('/todo')

    def post(self,request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['pk'])
        try:
            to_delete = user.todoitems_set.get(pk=request.POST['finished_item'])        
        except MultiValueDictKeyError:
            none_completed = "Nesplnil jsi zadny ukol!"
            return render(request, 'todo/detail.html', {'user': user, 'error_msg': none_completed})
        else:
            print(to_delete)
            to_delete.delete()
            user.save()
            return render(request, 'todo/detail.html', {'user': user})