from django.db import models


# Create your models here.
class ContactFormModel(models.Model):
    user_name = models.CharField(max_length=120)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.user_name
