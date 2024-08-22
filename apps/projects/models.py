import uuid
from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.timezone import now
import markdown


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(default=now, null=False, editable=False)
    last_modified_at = models.DateTimeField(default=now, null=False, editable=False)
    deleted_at = models.DateField(null=True, blank=True, editable=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='projects')  # Add ManyToManyField

    def __str__(self):
        return self.name

    def description_html(self):
        md = markdown.Markdown(extensions=["fenced_code"])
        return md.convert(self.description)

    def url(self):
        return reverse_lazy('project', kwargs={'pk': self.id})

    def settings_url(self):
        return reverse_lazy('project-settings', kwargs={'pk': self.id})
