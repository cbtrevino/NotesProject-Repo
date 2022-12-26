from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, null=True, default=1, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' | ' + self.user.username

    class Meta:
        ordering = ('title', 'content')