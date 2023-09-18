from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def index(request):
    context = {
        'all_shows' : Show.objects.all()
    }
    return render(request, 'index.html', context)

def new_show(request):
    return render(request, 'shows.html')

def create_show(request):
    print(request.POST)
    Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description'],
    )
    return redirect('/')

def show_id(request, show_id):
    this_show = Show.objects.get(id = show_id)
    context = {
        "show_info" : this_show
    }
    return render(request,'show.html', context)

def delete_show(request, show_id):
    show_to_delete = Show.objects.filter(id = show_id)
    show_to_delete.delete()
    return redirect('/')

def edit_show(request, show_id):
    edit_show = Show.objects.get(id = show_id)
    context = {
        "show_info" : edit_show
    }
    return render(request, 'edit.html', context)

def update_show(request, show_id):
    print(request.POST)
    show_id = Show.objects.get(id = show_id)
    show_id.title = request.POST['title']
    show_id.network = request.POST['network']
    show_id.release_date = request.POST['release_date']
    show_id.description = request.POST['description']
    show_id.save()
    return redirect('/')
