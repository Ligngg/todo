from django.shortcuts import render,redirect
from django.urls import reverse_lazy


from .models import Task
from .forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView ,DeleteView
# Create your views here.


class Tasktaskview(ListView):
    model=Task
    template_name='index.html'
    context_object_name='task'

class TaskDetailView(DetailView):
    model=Task
    template_name='detail.html'
    context_object_name='task'



class TaskUpdateView(UpdateView):
    model=Task
    template_name='update.html'
    context_object_name='task'
    fields=('task1','priority1','date1')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model=Task
    template_name='delete.html'
    success_url=reverse_lazy('cbvhome')





def index(request):
    detail = Task.objects.all()
    if request.method=='POST':
        task3=request.POST.get('task2','')
        priority3=request.POST.get('priority2','')
        date3=request.POST.get('date2','')
        taskk=Task(task1=task3,priority1=priority3,date1=date3)
        taskk.save()
    return render(request,'index.html',{'detail':detail})

def delete(request,id):
    task=Task.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    tk=Task.objects.get(id=id)
    tf=TodoForm(request.POST or None, instance=tk)
    if tf.is_valid():
        tf.save()
        return redirect('/')
    return render(request,'edit.html',{"tf1":tf,'tk1':tk})