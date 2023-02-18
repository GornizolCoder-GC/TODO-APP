from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from todoapp.form import CreateForm
from todoapp.models import TodoApp


def homepage(request):
    todolist = TodoApp.objects.all().order_by('created')

    return render(request, 'home.html', {'todolist':todolist})

def create(request):
    form = CreateForm()

    if request.method == 'POST':
        create_form = CreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
        return redirect('home')

    return render(request, 'create.html', {'form':form})

def update(request, id):
    todo = TodoApp.objects.get(id=id)
    updateForm =CreateForm(instance=todo)

    if request.method == 'POST':
        updateForm = CreateForm(request.POST, instance=todo)

        if updateForm.is_valid():
            updateForm.save()

        return redirect('home')

    return render(request, 'update.html', {'form':updateForm})


class TodoDeleteView(DeleteView):
    model = TodoApp
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
