from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
# this pulls in data from the database
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy

# Create your views here.


# ------------------- index function based view is not used, replaced by the class based view "ListView" below----------------------
def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('drinks/index.html')
    # this is the drinks folder within the templates folder!
    context = {
        'item_list':item_list,
        # passing in item_list as "item_list"
    }
    return render(request,'drinks/index.html',context)
    # passes context into a template

class IndexClassView(ListView):
    # inherit from ListView class from django, since we are presenting a list of drinks
    model = Item;
    # pass in a whole class" Item", vs. specific list in the function view above
    template_name = 'drinks/index.html'
    context_object_name = 'item_list'

    
# ------------------- using detail function view to pass in more context----------------------

def detail(request, item_id):
    # in drinks's urls.py, item_id is passed in through the inputed url
    item = Item.objects.get(pk=item_id)
    # pk = primary key
    context = {
        'object':item,
        'ingredient_list':item.item_ingredients.split(","),
    }
    return render(request, 'drinks/detail.html', context)

class DetailClassView(DetailView):
    model = Item;
    template_name = 'drinks/detail.html'

# --------------replaced by class based view below------------------
def create_item(request):
    form = ItemForm(request.POST or None)
    # create object "form" from forms.py which defines fields and pulls in django form template
    if form.is_valid():
        form.save()
        return redirect('drinks:index')
    
    return render(request, 'drinks/item-form.html',{'form':form})
    #render object form with fields defined in forms.py into item-form.html 

class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image', 'item_ingredients']
    template_name = 'drinks/item-form.html'
    # field names from the model Item
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        # user_name field will be updated automaticlly here with the user who puts in the request to create this item
        return super().form_valid(form)
    # Createview is the super class, CreateItem is the subclass, super() is calling form_valid() in CreateView


# --------------replaced by class based view below------------------

def update_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)
    # passes the selected item into the form
    # post both updated fields & uploaded files
    if form.is_valid():
        form.save()
        return redirect('drinks:index')
    
    return render(request, 'drinks/item-form.html', {'form':form, 'item':item})



class DeleteClassView(DeleteView):
    model = Item;
    template_name = 'drinks/item-delete.html'
    success_url = reverse_lazy('drinks:index')