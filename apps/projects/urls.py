from django.urls import path
from .views import project, project_settings


urlpatterns = [
    path("<str:pk>/", project, name="project"),
    path("<str:pk>/settings", project_settings, name="project-settings")
]
