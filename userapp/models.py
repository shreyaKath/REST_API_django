from django.db import models

class Users(models.Model):
    id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    user_id = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.id
