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
from django.db.models import Q 

'''

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())
  
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

#View item
def item_detail_view(request, primary_key):
  item = get_object_or_404(Item, pk=primary_key)
  return render(request, '/item_detail.html', context={'item': item})

# Home Login page
def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

#@login_required
#Home page
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

#@login_required
def item_detail_view(request, primary_key):
  item = get_object_or_404(Item, pk=primary_key)
  return render(request, '/item_detail.html', context={'item': item})

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
def create_item(request, pk):
    item_instance = get_object_or_404(Item, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = Item(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #item_instance.due_back = form.cleaned_data['renewal_date']
            item_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('item'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = ItemCreate()

    context = {
        'form': form,
        'item_instance': item_instance,
    }

    return render(request, 'item_form.html', context)

#@login_required
def edit_item(request, pk):
    item_instance = get_object_or_404(Item, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = Item(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            item_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('inventory'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = ItemCreate(initial={'item': item})

    context = {
        'form': form,
        'item_instance': item_instance,
    }

    return render(request, 'item_form.html', context)

'''

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


# Home Login page
def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

@login_required
def item_detail_view(request, primary_key):
  item = get_object_or_404(Item, pk=primary_key)
  return render(request, '/item_detail.html', context={'item': item})

#render pages
@login_required
def members(request):
  template = loader.get_template('inventory.html')
  return HttpResponse(template.render())


def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())


def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))


@login_required
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

@login_required
def create_item(request, pk):
    item_instance = get_object_or_404(Item, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = Item(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            #item_instance.due_back = form.cleaned_data['renewal_date']
            item_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('item'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = ItemCreate()

    context = {
        'form': form,
        'item_instance': item_instance,
    }

    return render(request, 'item_form.html', context)

@login_required
def edit_item(request, pk):
    item_instance = get_object_or_404(Item, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = Item(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            item_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('inventory'))

    # If this is a GET (or any other method) create the default form.
    else:
        form = ItemCreate(initial={'item': item})

    context = {
        'form': form,
        'item_instance': item_instance,
    }

    return render(request, 'item_form.html', context)
    