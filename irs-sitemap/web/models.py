from django.db import models

# Create your models here.

class Member(models.Model):
    

    def __str__(self):
        return self.firstname + " " + self.lastname
