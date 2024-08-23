# hostel/models.py

from django.db import models

class Application(models.Model):
    stud_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    adhar_number = models.CharField(max_length=12)
    caste = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    address = models.TextField()
    location = models.CharField(max_length=100)
    family_details = models.TextField() #defult= True
    family_annual_income = models.DecimalField(max_digits=10, decimal_places=2)
    father_name = models.CharField(max_length=255)
    passport = models.FileField(upload_to='documents/')
    income_certificate = models.FileField(upload_to='documents/')
    caste_certificate = models.FileField(upload_to='documents/')
    domicile_certificate = models.FileField(upload_to='documents/')
    adhar_card = models.FileField(upload_to='documents/')
    hostel_form = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.stud_name
