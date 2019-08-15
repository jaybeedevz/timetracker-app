from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField
from branches.models import Specialization
from branches.models import Clinic


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

SCHEDULE_DAY_CHOICES =(
    ('monday', 'Monday'),
    ('tuesday', 'Tuesday'),
    ('wenesday', 'Wenesday'),
    ('thursday', 'Thursday'),
    ('friday', 'Friday'),
    ('saturday', 'Saturday'),
    ('sunday', 'Sunday'),   
)

SCHEDULE_TIME_IN_CHOICES =(

    ('12:00AM', '12:00AM'),
    ('01:00AM', '01:00AM'),
    ('02:00AM', '02:00AM'),
    ('03:00AM', '03:00AM'),
    ('04:00AM', '04:00AM'),
    ('05:00AM', '05:00AM'),
    ('06:00AM', '06:00AM'),
    ('07:00AM', '07:00AM'),
    ('08:00AM', '08:00AM'),
    ('09:00AM', '09:00AM'),
    ('10:00AM', '10:00AM'),
    ('11:00AM', '11:00AM'),
    ('12:00PM', '12:00PM'),
    ('01:00PM', '01:00PM'),
    ('02:00PM', '02:00PM'),
    ('03:00PM', '03:00PM'),
    ('04:00PM', '04:00PM'),
    ('05:00PM', '05:00PM'),
    ('06:00PM', '06:00PM'),
    ('07:00PM', '07:00PM'),
    ('08:00PM', '08:00PM'),
    ('09:00PM', '09:00PM'),
    ('10:00PM', '10:00PM'),
    ('11:00PM', '11:00PM'),
  
)


SCHEDULE_TIME_OUT_CHOICES =(

    ('12:00AM', '12:00AM'),
    ('01:00AM', '01:00AM'),
    ('02:00AM', '02:00AM'),
    ('03:00AM', '03:00AM'),
    ('04:00AM', '04:00AM'),
    ('05:00AM', '05:00AM'),
    ('06:00AM', '06:00AM'),
    ('07:00AM', '07:00AM'),
    ('08:00AM', '08:00AM'),
    ('09:00AM', '09:00AM'),
    ('10:00AM', '10:00AM'),
    ('11:00AM', '11:00AM'),
    ('12:00PM', '12:00PM'),
    ('01:00PM', '01:00PM'),
    ('02:00PM', '02:00PM'),
    ('03:00PM', '03:00PM'),
    ('04:00PM', '04:00PM'),
    ('05:00PM', '05:00PM'),
    ('06:00PM', '06:00PM'),
    ('07:00PM', '07:00PM'),
    ('08:00PM', '08:00PM'),
    ('09:00PM', '09:00PM'),
    ('10:00PM', '10:00PM'),
    ('11:00PM', '11:00PM'),
  
)


class Physician(models.Model):
    clinic =            models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name='clinics')
    specialization =    models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='specializations')
    first_name =        models.CharField(max_length=30)
    last_name =         models.CharField(max_length=30)

    email =             models.EmailField(unique=True)
    contact_num =       models.CharField(max_length=11)
    status =            models.CharField(max_length=60, choices=STATUS_CHOICES, null=True)
    date_join =         models.DateTimeField(auto_now_add=True, blank=True)
    is_active =         models.BooleanField(default=True)
    
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Schedule(models.Model):
    schedule_day =         models.CharField(max_length=60, choices=SCHEDULE_DAY_CHOICES, null=True)
    schedule_time_in =     models.CharField(max_length=60, choices=SCHEDULE_TIME_IN_CHOICES, null=True)
    schedule_time_out =    models.CharField(max_length=60, choices=SCHEDULE_TIME_OUT_CHOICES, null=True)
    physician =            models.ForeignKey(Physician, on_delete=models.CASCADE, related_name='physicians')

    def __str__(self):
        return "%s %s" % (self.physician.first_name, self.physician.last_name)