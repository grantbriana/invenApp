from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from .models import Item
from .forms import Item
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required


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

#@login_required
def inventory(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_items = Item.objects.all().count()
    item_obj = Item.objects.all()


    context = {
        'num_items': num_items,
        'items': item_obj,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'inventory.html', context=context)

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

#inventory page
#Search Functionality
class SearchResultsView(ListView):
    model = Item
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get("q")
        object_list = Item.objects.filter(
            Q(name__icontains=query) | Q(id__icontains=query)
        )
        return object_list

#Item Model Views
class ItemListView(generic.DetailView):
    model = Item

class ItemDetailView(generic.DetailView):
    model = Item


#CRUD Functionality
class ItemCreate(CreateView):
    model = Item
    fields = ['id', 'name', 'inventory']

class ItemUpdate(UpdateView):
    model = Item
    fields = ['id', 'name', 'inventory']

class ItemDelete(DeleteView):
    model = Item
    success_url = "/inventory"


#@login_required
def item_detail_view(request, primary_key):
  item = get_object_or_404(Item, pk=primary_key)
  return render(request, '/item_detail.html', context={'item': item})