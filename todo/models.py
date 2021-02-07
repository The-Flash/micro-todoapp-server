from django.db import models

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey("authentication.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title