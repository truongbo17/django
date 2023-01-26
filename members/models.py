from django.db import models


# Create your models here.
class PostForm(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
