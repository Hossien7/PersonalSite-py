from django.db import models


class projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    address = models.CharField(max_length=255)
    image = models.ImageField(upload_to="projects")


    def __str__(self):
        return self.title
