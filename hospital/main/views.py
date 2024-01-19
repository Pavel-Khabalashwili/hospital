from django.shortcuts import render, redirect, get_object_or_404
from .models import Applications
from .forms import ApplicationsForm
from django.views.generic import DetailView
from django.contrib.auth import authenticate, login, logout


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/')
        return view_func(request, *args, **kwargs)
    return wrapper

# @login_required
class ApplicationDetailView(DetailView):
    model = Applications
    template_name = 'main/aplctn.html'
    context_object_name = 'desk'

    def get_object(self):
        title = self.kwargs.get('title')
        return get_object_or_404(Applications, title=title)
    
    
def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todo')  # перенаправляем на страницу todo после удачного входа
        else:
            return render(request, 'main/log.html',{'error': 'Invalid login'})  # передаем сообщение об ошибке в шаблон log.html
    else:
        return render(request, 'main/log.html')  

@login_required
def todo(request):
    entries = Applications.objects.filter(user=request.user)  # Фильтруем заявки по текущему пользователю
    return render(request, 'main/todo.html', {'entries': entries})

@login_required
def create(request):
    if request.method == 'POST':
        form = ApplicationsForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user  # Привязываем заявку к текущему пользователю
            application.save()
            return redirect('todo')
    else:
        form = ApplicationsForm()
    context = {'form': form}
    return render(request, 'main/create-aplctn.html', context)

@login_required
def aplctn(request):
    return render(request, 'main/aplctn.html')


def delete_desk(request, pk):
    desk = get_object_or_404(Applications, pk=pk)
    if request.method == 'POST':
        desk.delete()
        return redirect('todo')
    return render(request, 'todo.html', {'desk': desk})

def change_status(request, pk):
    if request.method == 'POST':
        desk = get_object_or_404(Applications, pk=pk)
        desk.status = True
        desk.save()
        return redirect('todo')