from django.shortcuts import render, get_object_or_404
from .models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'index.html', context)

def detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    context = {
        'project':project
    }
    return render(request, 'detail.html', context)

def contact(request):
    return render(request, 'contact.html')