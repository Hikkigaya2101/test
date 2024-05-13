from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
from .models import Position, Worker
from .forms import WorkerForm,PositionForm
import asyncio
from datetime import datetime

def index(request):
    positions = Position.objects.all()
    workers = Worker.objects.all()
    context = {
        'positions': positions,
        'workers': workers
    }
    return render(request,'myapp/index.html',context)


async def create_position():
    person = await Position.objects.acreate(position_name="Начальник отделения")
    print(person.position_name)

def del_position():
    person = Position.objects.get(position_name="старший инженер")
    person.delete()
def post_position(request):
    if request.method =="POST":
        form = PositionForm(request.POST)
        form.save()
        redirect('index.html')
    form = PositionForm()
    data = {
        'form':form,

    }

    return render(request,'myapp/index.html',data)

def post_worker(request):
    if request.method =="POST":
        form = WorkerForm(request.POST)
        if form.is_valid():

           form.save()
        else: print('error')

    redirect('index.html')
    form = WorkerForm
    data = {
        'form':form,

    }

    return render(request,'myapp/index.html',data)



# изменение данных в бд
def edit(request, id):
    try:
        positions = Position.objects.get(id=id)

        if request.method == "POST":
            positions.position_name = request.POST.get("name")

            positions.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "index.html", {"positions": positions})
    except Position.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


# удаление данных из бд
def delete(request, id):
    try:
        workers = Worker.objects.get(id=id)
        workers.delete()
        return HttpResponseRedirect("/")
    except Worker.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def average():
    workers = Worker.objects.all()
    data = workers.born_date
    print(data)

