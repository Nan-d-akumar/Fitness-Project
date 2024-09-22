from django.db import models
from django.contrib.auth.models import User

# Create your models here.
roles = (('male','male'),('female','female'),('other','other'),('',''))
class Tbl_staff(models.Model):
    staff_fname=models.CharField(max_length=10)
    staff_lname = models.CharField(max_length=10)
    staff_age = models.CharField(max_length=3)
    staff_gender = models.CharField(max_length=10,choices=roles,default='')
    staff_phone = models.CharField(max_length=10)
    staff_email = models.EmailField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    staff_status = models.BooleanField(default=True)
    def __str__(self):
        return self.staff_fname

