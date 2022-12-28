from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Item
from .forms import Item
from django.views.generic.edit import CreateView, UpdateView, DeleteView


#CRUD Functionality
class ItemCreate(CreateView):
    model = Item
    fields = ['id', 'name', 'inventory']

class ItemUpdate(UpdateView):
    model = Item
    fields = ['id', 'name', 'inventory']

class ItemDelete(DeleteView):
    model = Item
    success_url = "/hello_azure/index.html"


def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name }
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')

