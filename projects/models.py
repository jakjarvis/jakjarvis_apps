from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='projects/images/')
    url = models.URLField(blank=True)
    view = models.CharField(max_length=50, blank=True)
    button_text = models.CharField(max_length=30, blank=True)
    button_view = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.title