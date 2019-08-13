from django.db import models



class Specialization(models.Model):
    specialty = models.CharField(max_length=60)
    sub_specialty = models.CharField(max_length=60)

class Clinic(models.Model):
    name  =     models.CharField(max_length=30)
    address =   models.TextField(max_length=120)
    
