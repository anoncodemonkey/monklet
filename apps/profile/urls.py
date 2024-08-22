from django.urls import path
from .views import profile, profile_edit


urlpatterns = [
    path("", profile, name="profile"),
    path('<int:pk>/edit', profile_edit, name='profile-edit'),
]
