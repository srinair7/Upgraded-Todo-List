from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
<<<<<<< HEAD
=======
    image_url = models.CharField(max_length=2083, null=True)
    image = models.ImageField(upload_to='pictures', blank=True)
>>>>>>> fde8ace... added image feature

    def __str__(self):
        return self.text