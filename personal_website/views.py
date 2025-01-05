from django.shortcuts import render
from projects_app.models import projects

project = projects.objects.all()


def home(request):
    return render(request, 'index.html', context={'projects': project})
