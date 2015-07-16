from django.contrib.auth.models import User
from django.db import models

class Entry(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100, null=True, blank=True)
    calories = models.IntegerField()
    logged_at = models.DateTimeField(auto_now_add=True)
