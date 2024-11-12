import datetime
from django.utils import timezone
from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    author = models.CharField(max_length=100)
    content = models.TextField()
    # image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
class Comment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.content