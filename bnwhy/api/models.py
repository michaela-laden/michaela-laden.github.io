from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)   #Sets posts created time/date
    author = models.ForeignKey(User, on_delete=models.CASCADE) #If a user is deleted then their posts are deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts-detail', kwargs={'pk':self.pk})