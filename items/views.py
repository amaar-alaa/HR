from django.shortcuts import render, redirect,get_object_or_404
from django.views import generic
from .models import *
from .form import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

# for product
@login_required(redirect_field_name='login')
def index(request):
    products = Product.objects.all()
    curn=Curn.objects.first()
    form=CurnForm(instance=curn)
    return render(request, 'items/index.html', {'products': products,'curn':curn,'form':form})

class ItemDetail(generic.DetailView):
    model = Product
    login_required=True
    template_name = 'items/item_dit.html'

@login_required(redirect_field_name='login')
def create(request):
    if request.method == "POST" and 'save' in request.POST:
        form = ProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, 'Item was  Addes Successfully!')
                return redirect('index')
            except:
                pass
    elif request.method == "POST" and 'save2' in request.POST:
        form = ProductForm(request.POST, request.FILES or None)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, 'Item was  Added Successfully!')
                form = ProductForm()
                return render(request, 'items/create.html', {'form': form})
            except:
                pass        
    else:
         form = ProductForm()
         return render(request, 'items/create.html', {'form': form})


@login_required(redirect_field_name='login')
def edit(request, id):
    product = get_object_or_404(Product,id=id)
    form =ProductForm(instance=product)
    return render(request, 'items/edit.html', {'product': product,'form':form})


@login_required(redirect_field_name='login')
def update(request, id):
    
    product = get_object_or_404(Product,id=id)
    form = ProductForm(request.POST, request.FILES or None ,instance=product)
    if form.is_valid():
        form.save()
        messages.info(request, f'{product.name} was  updated Successfully!')
        return redirect("index")
    return render(request, 'items/edit.html', {'form': form})

@login_required(redirect_field_name='login')
def destroy(request, id):
    product = get_object_or_404(Product,id=id)
   
    product.delete() 
    messages.error(request, f'{product.name} is delete')
    return redirect("index")


# for curency
@login_required(redirect_field_name='login')
def update_curn(request, id):
    
    product = get_object_or_404(Curn,id=id)
    form = CurnForm(request.POST,instance=product)
    if form.is_valid():
        form.save()
        messages.info(request, 'currency was  updated Successfully!')
        return redirect("index")
    messages.info(request, 'currency was  updated Successfully!')   
    return redirect("index")


## For depart
@login_required(redirect_field_name='login')
def depart_create(request):
    if request.method == "POST" and 'save' in request.POST:
        form = DepartForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, 'depart was  Addes Successfully!')
                return redirect('depart_create')
            except:
                pass
    elif request.method == "POST" and 'save2' in request.POST:
        form = DepartForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, 'Item was  Added Successfully!')
                form = DepartForm()
                depart=Depart.objects.all()
                return render(request, 'depart/depart_create.html', {'depart':depart,'form': form})
            except:
                pass        
    else:
         form = DepartForm()
         depart=Depart.objects.all()
         return render(request, 'depart/depart_create.html', {'form': form ,'depart':depart})

def depart_edit(request,id):
    depart=get_object_or_404(Depart,id=id)
    form=DepartForm(instance=depart)
    return render(request,'depart/depart_edit.html',{'form':form,'depart':depart})

def depart_update(request,id):

    depart=get_object_or_404(Depart,id=id)
    form=DepartForm(request.POST,instance=depart)
    if form.is_valid():
        form.save()
        messages.success(request,f'{depart.name} was  updated Successfully! ')
        return redirect('depart_create')
    messages.success(request,'Something Is Wrong ! ')    
    return render(request,'depart/depart_edit.html',{'form':form,'depart':depart})    


@login_required(redirect_field_name='login')
def depart_delete(request,id):
    depart=get_object_or_404(Depart,id=id)
    depart.delete()
    messages.error(request, f'{depart.name} is deleted')
    return redirect("depart_create")

## For Unit
@login_required(redirect_field_name='login')
def unit_create(request):
    if request.method == "POST" and 'save' in request.POST:
        form = UnitForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.info(request, 'New Unit was  Addes Successfully!')
                return redirect('unit_create')
            except:
                pass
    
    form = UnitForm()
    depart=Unit.objects.all()
    return render(request, 'unit/unit_create.html', {'form': form ,'depart':depart})

def unit_edit(request,id):
    depart=get_object_or_404(Unit,id=id)
    form=UnitForm(instance=depart)
    return render(request,'unit/unit_edit.html',{'form':form,'depart':depart})

def unit_update(request,id):
    depart=get_object_or_404(Unit,id=id)
    form=DepartForm(request.POST,instance=depart)
    if form.is_valid():
        form.save()
        messages.success(request,f'{depart.name} was  updated Successfully! ')
        return redirect('unit_create')
    messages.success(request,'Something Is Wrong ! ')    
    return render(request,'unit/unit_edit.html',{'form':form,'depart':depart})    

def unit_delete(request,id):
    depart=get_object_or_404(Unit,id=id)
    depart.delete()
    messages.error(request, f'{depart.name} is deleted')
    return redirect("unit_create")     

    
         