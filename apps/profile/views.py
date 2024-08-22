from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from web_project.template_helpers.theme import TemplateHelper
from django.core.exceptions import ObjectDoesNotExist

from apps.projects.models import Project
from .models import Profile


@login_required
def profile(request):
    try:
        profile = request.user.profile
    except ObjectDoesNotExist:
        profile = Profile(user=request.user)
        profile.save()
    projects = Project.objects.filter(owner=request.user, deleted_at=None)
    ctx = {
        "projects": projects,
        "avatar_url": profile.avatar_url,
        "date_joined": request.user.date_joined.strftime("%d %b, %Y")
    }
    ctx['layout_path'] = TemplateHelper.set_layout("layout_vertical.html", ctx)
    print(ctx)
    return render(request, "profile/profile.html", ctx)

@login_required
def profile_edit(request, pk):
    profile = Profile.objects.get(pk=pk)
    if profile.user.id != request.user.id and not profile.user.is_superuser:
        return redirect('profile')
    ctx = {
        'profile': profile,
        'layout_path': TemplateHelper.set_layout("layout_vertical.html", {})
    }
    return render(request, "profile/profile-edit.html", ctx)
