from django.db import models
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
