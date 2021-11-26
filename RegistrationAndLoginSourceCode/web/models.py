from django.db import models

# Create your models here.

class Member(models.Model):
<<<<<<< HEAD:RegistrationAndLoginSourceCode/web/models.py
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
=======
    
>>>>>>> 83d1d6f (IRS sitemap task):web/models.py

    def __str__(self):
        return self.firstname + " " + self.lastname