from django.db import models

# Create your models here.
class Login(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return f'[{self.pk}]{self.email}'