from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import render,redirect ,get_object_or_404
from .models import *
from .form import *
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(redirect_field_name='login')
def addtodo(request):
    
    x = request.POST['content']
    new_item = TodoListItem(content = x)
    new_item.for_how=request.user.username
    new_item.save()
    return redirect("repo_list")

@login_required(redirect_field_name='login')
def deleteTodoView(request, id):
    y = TodoListItem.objects.get(id= id)
    y.delete()    
    return redirect("repo_list")

@login_required(redirect_field_name='login')
def checkTodoView(request, id):
    y = TodoListItem.objects.get(id= id)
    if y.active == True :
       y.active=False 
       y.save()
       
    else :
        y.active=True    
        y.save()
         
    return redirect("repo_list")

# for Reports

@login_required(redirect_field_name='login')
def RepoList(request):
    repo_list = Repo.objects.all().order_by('-created_on')
    todo=TodoListItem.objects.all()
    return render(request,'repo/repolist.html',{'todo':todo,'repo_list':repo_list})


# add login reqierd in url.py or atturibut in side class 
class RepoDetail(generic.DetailView):
    model = Repo
    login_required=True
    template_name = 'repo/repodit.html'


@login_required(redirect_field_name='login')
def repo_edit(request, id):
    product = get_object_or_404(Repo,id=id)
    form =RepoForm(instance=product)
    return render(request, 'repo/repo_edit.html', {'product': product,'form':form})


@login_required(redirect_field_name='login')
def repo_update(request, id):
    
    product = get_object_or_404(Repo,id=id)
    form = RepoForm(request.POST ,instance=product)
    if form.is_valid():
        form.save()
        messages.info(request, f'{product.title} was  edit  Successfully!')
        return redirect("repo_list")
    messages.info(request, 'Something is wrong !')    
    return render(request, 'repo/repo_edit.html', {'form': form})


class RepoCreate(generic.CreateView):
    login_required=True
    def get(self, request, *args, **kwargs):
        context = {'form': RepoForm()}
        return render(request, 'repo/create.html', context)

    def post(self, request, *args, **kwargs):
        form = RepoForm(request.POST)
        if form.is_valid():
            repo = form.save(commit=False)
            repo.author=request.user.username
            repo.save()
            messages.success(request, 'Your Report has been sent successfully!')
            return redirect("repo_list")
        messages.error(request, 'SomeThing is wrong !')    
        return render(request, 'repo/create.html', {'form': form})      

        
          