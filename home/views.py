from django.shortcuts import render
from django.http import HttpResponse

from home.forms import ContactForm
from django.contrib import messages

from home.models import Teacher
# Create your views here.


def home(request):

    teachers = Teacher.objects.all()

    if request.method == 'POST':
        # POST here means all data from frontend
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The form has been submitted!')
    else:
        form = ContactForm()

    context = {
        'form': form,
        "teachers": teachers,
    }
    return render(request, 'home/index.html', context)


def about(request):
    return render(request, 'home/about.html')


def teacher(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, 'home/teacher.html', context)
