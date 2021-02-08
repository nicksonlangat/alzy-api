from django.db import models

# Create your models here.
class Reminder(models.Model):
    title=models.CharField(max_length=20)
    details=models.TextField()
    deadline=models.IntegerField()

    def __str__(self):
        return self.title

class File(models.Model):
    name=models.CharField(max_length=10)
    image = models.FileField(blank=False, null=False)
    def __str__(self):
        return self.name
