import hashlib

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from web_project.template_helpers.theme import TemplateHelper
from django.urls import reverse_lazy

from .models import Project
from .forms import ProjectForm

def menu(project):
    return {
        'menu': [
            {'url': '/profile', 'icon': 'menu-icon tf-icons ri-home-line', 'name': 'Profile'},
            {'url': project.url(), 'icon': 'menu-icon tf-icons ri-folders-line', 'name': project.name},
        ]
    }

@login_required
def project(request, pk):
    proj = get_object_or_404(Project, pk=pk, owner=request.user)
    ctx = {
        "project": proj,
        "menu_data": menu(proj)
    }
    return render(request, "projects/project.html", ctx)


@login_required
def project_settings(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect("project_list")
    else:
        form = ProjectForm(instance=project)
    return render(request, "projects/update.html", {"form": form})


@login_required
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == "POST":
        project.delete()
        return redirect("project_list")
    return render(request, "projects/delete.html", {"project": project})
