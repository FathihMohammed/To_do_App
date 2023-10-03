from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import task
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
# Create your views here.
class clistview(ListView):
    model=task
    template_name = 'home.html'
    context_object_name = 'task'
class cdetailview(DetailView):
    model=task
    template_name = 'details.html'
    context_object_name = 'i'
class cupdateview(UpdateView):
    model=task
    template_name = 'edit.html'
    context_object_name = 'i'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbdetails',kwargs={'pk':self.object.id})
class cdeleteview(DeleteView):
    model=task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')
def home(request):
    t2 = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        t1=task(name=name,priority=priority,date=date)
        t1.save();
    return render(request,'home.html',{"task":t2})
def delete(request,taskid):
    t3=task.objects.get(id=taskid)
    if request.method=='POST':
        t3.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    t1=task.objects.get(id=id)
    f=TodoForm(request.POST or None,instance=t1)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'t1':t1})