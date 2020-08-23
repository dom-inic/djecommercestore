from django.shortcuts import render
from . forms import NewItemForm
from django.shortcuts import reverse
from . models import Item
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

def home(request):
    """ homepage """
    items =Item.objects.order_by('date_added')
    paginator = Paginator(items, 3) #show three items per page 
    page = request.GET.get('page')
    items = paginator.get_page(page)
    template_name = 'shop/base.html'
    context= {'items': items}
    return render(request, template_name, context)

def addnewitem(request):
    """ allow sellers to an new item """
    if request.method != 'POST':
        # no data has been submitted, create a new form
        form = NewItemForm()
    else:
        # data has been sumitted, time to process the data
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    template_name = 'shop/newitem.html'
    context = {'form': form}
    return render(request, template_name, context)

def detail(request, item_id):
    """ allow customers to get access to details for a product """
    item = Item.objects.get(pk=item_id)
    template_name = 'shop/item_detail.html'
    context = {'item': item }
    return render(request, template_name, context)

def cartpage(request):
    """ show items added to cart """
    template_name = 'shop/cart_page.html'
    return render(request, template_name)




