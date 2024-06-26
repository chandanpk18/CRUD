from django.db import models

# Create your models here.

class Stdents(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.CharField(max_length=15)
    query=models.CharField(max_length=150)

    def __str__(self):
        return str(self.id)