from django.db import models


# Create your models here.
class Upload(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField()
    body = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=120)
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s, %s" % (self.parent_id, self.name)
