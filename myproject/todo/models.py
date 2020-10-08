from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pictures', blank=True)

    def __str__(self):
        return self.text