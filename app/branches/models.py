from django.db import models

STATUS_CHOICES =(
    ('coming', 'Coming'),
    ('on going', 'On Going'),
    ('not coming', 'Not Coming'),
    ('reliver', 'Reliver'),
    ('on call', 'On Call'),
    ('not sure', 'Not Sure'),
    ('leave', 'Leave'),
    ('Out', 'Out'),
)

class Physician(models.Model):

    specialization =    models.ForeignKey('Specialization', on_delete=models.CASCADE)
    first_name =        models.CharField(max_length=30)
    last_name =         models.CharField(max_length=30)
    email =             models.EmailField()
    contact_num =       models.IntegerField()
    is_active =         models.BooleanField(default=True)
    status =            models.CharField(max_length=60, choices=STATUS_CHOICES, null=True)
    date_join =         models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Specialization(models.Model):
    specialty = models.CharField(max_length=60)
    sub_specialty = models.CharField(max_length=60)
