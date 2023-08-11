from django.db import models

# Create your models here.
class tbl_hospital(models.Model):
    Emp_id=models.IntegerField()
    Doctor=models.CharField(max_length=100)
    Specialization=models.CharField(max_length=100)
    Salary=models.IntegerField()
    Experience=models.CharField(max_length=100)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=100)
    class Meta:
        db_table="tbl_hospital"


class tbl_patient(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    date=models.DateField(max_length=30)
    gender=models.CharField(max_length=50)

    class Meta:
        db_table = "tbl_patient"
