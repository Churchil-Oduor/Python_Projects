from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    age = models.IntegerField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.reg_no