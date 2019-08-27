from django.db import models




class Specialization(models.Model):
    specialty = models.CharField(max_length=60)
    desc = models.TextField(max_length=120)



class Clinic(models.Model):
    branch_name  =     models.CharField(max_length=30)
    address =          models.TextField(max_length=120)

    
    

    