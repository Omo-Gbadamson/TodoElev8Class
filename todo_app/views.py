from cgitb import text
from urllib import request
from django.shortcuts import render, redirect
# Here is where the data from the backend are being imported
from .models import Task

# Create your views here.
# this home function is what we caled in the urls where we extended from


def home(request):
    '''Renders the home when user is logged in'''
    my_tasks = Task.objects.all()
    return render(request, 'users.html', {'my_tasks': my_tasks})


def index(request):
    '''This will render the index page'''
    return render(request, 'index.html')


def log(request):
    '''This will should render the log page'''
    return render(request, 'log.html')


def edit(request):
    '''This will render the edit page'''
    return render(request, 'edit.html')


def profile(request):
    '''This will render the profile page'''
    return render(request, 'profile.html')


def signup(request):
    '''This will render the signup page'''
    return render(request, 'sign.html')


def add_task(request):
    '''This should add up task'''
    # This line will help us to Get what users have typed just like the DOM in js, the 'task' is coming from the name assigned to the form
    # the GET method helps us to get items on the front end (just like request.GET.get())
    # the POST helps us to post data (just like request.POST.get)
    # we can now pass a condition that checks users action
    if request.method == 'POST':
        # the condition we are working for
        task_passed = request.POST.get('task')
        if task_passed:
            new_task = Task()
            new_task.name = task_passed
            new_task.save()

    return redirect('home')


def delete(request):
    '''Let's delete somethings '''
    deleted_item = request.GET.get('to_delete')
    item_to_delete = Task.objects.get(id=deleted_item)
    item_to_delete.delete()
    return redirect('home')


def edit(request):
    '''This wlii help us to edit'''
    # edit_item = request.GET.get('editable')
    # item_edit = Task.objects.get(id=edit_item)
    # new_edit = item_edit.replace()
    # new_edit.save()
    # return redirect('home')
    # print(item_edit)
    if request.method == 'POST':
        edit_item = request.POST.get('editable')
        id = request.POST.get('edit_id')
        item_to_edit = Task.objects.get(id=id)
        item_to_edit.name = edit_item
        item_to_edit.save()
        return redirect('home')
