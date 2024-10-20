from django.db import models

# Create your models here.

class employe(models.Model):
    name=models.TextField()
    address=models.TextField()
    position=models.TextField()
    salary=models.IntegerField()
    experiance=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField()
    empid=models.IntegerField()

    def __str__(self):
        return self.name