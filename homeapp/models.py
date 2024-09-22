from django.contrib.auth.models import User
from django.db import models
from datetime import date


roles = (('male', 'male'), ('female', 'female'), ('other', 'other'), ('', ''))


class Tbl_customer(models.Model):
    cust_fname = models.CharField(max_length=10)
    cust_lname = models.CharField(max_length=10)
    cust_age = models.CharField(max_length=3)
    cust_gender = models.CharField(max_length=10, choices=roles, default='')
    cust_height = models.CharField(max_length=3)
    cust_weight = models.CharField(max_length=3,null=True)
    cust_phone = models.CharField(max_length=10)
    cust_problem = models.TextField(max_length=100)
    cust_email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cust_status = models.BooleanField(default=True)

    def __str__(self):
        return self.cust_fname


class Tbl_Trainer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trainer_name = models.CharField(max_length=20)
    trainer_age = models.PositiveIntegerField()
    trainer_gender = models.CharField(max_length=10, choices=roles, default='')
    trainer_email = models.EmailField()
    trainer_phone = models.CharField(max_length=10)
    trainer_certificate = models.FileField(upload_to='trainer_certificates')
    level = (('', ''), ('level-1', 'level-1'), ('level-2', 'level-2'), ('level-3', 'level-3'), ('level-4', 'level-4'),
             ('level-5', 'level-5'), ('level-6', 'level-6'))
    trainer_level = models.CharField(max_length=20, choices=level, default='')
    trainer_image = models.ImageField(upload_to='trainer_images', default='')
    trainer_approval = models.BooleanField(default=False)
    trainer_status = models.BooleanField(default=False)

    def __str__(self):
        return self.trainer_name


class Tbl_Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_desc = models.TextField()
    category_image = models.ImageField(upload_to='category_image')

    def __str__(self):
        return self.category_name


roles = (('chest', 'chest'), ('shoulder', 'shoulder'), ('legs', 'legs'), ('back', 'back'), ('biceps', 'biceps'),
         ('triceps', 'triceps'), ('forearms', 'forearms'), ('abs', 'abs'), ('none', 'none'))


class Tbl_SubCategory(models.Model):
    category = models.ForeignKey(Tbl_Category, on_delete=models.CASCADE)
    sub_category_name = models.CharField(max_length=50, choices=roles, default='none')

    def __str__(self):
        return self.sub_category_name


class Tbl_tutorial(models.Model):
    sub_category_name = models.ForeignKey(Tbl_SubCategory, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos')
    reps = models.PositiveIntegerField(default=8)
    sets = models.PositiveIntegerField(default=3)
    rest_time = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.exercise_name

class Tbl_diet(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    staff = models.ForeignKey(User,on_delete=models.CASCADE,related_name='staff_user',null=True)
    status = models.BooleanField(default=False)
    diet = models.FileField(upload_to='diet_pdf',null=True)

    def __str__(self):
        return self.customer.first_name



class Tbl_card(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    expiry_date = models.DateField()

    def __str__(self):
        return self.customer.first_name

class Tbl_payment(models.Model):
    type = models.CharField(max_length=2,choices=(('D','Diet'),('T','Trainer')),default='none')
    card = models.ForeignKey(Tbl_card,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    amount = models.FloatField(null=True)
    pstatus = models.BooleanField(default=True)



    def __str__(self):
        return self.card.customer.first_name

class Tbl_trainer_assign(models.Model):
    trainer = models.ForeignKey(Tbl_Trainer,on_delete=models.CASCADE)
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Tbl_payment,on_delete=models.CASCADE)

    def __str__(self):
        return self.customer.first_name

# Leader Board

class Tbl_LeaderBoard(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.customer.first_name


class Tbl_Feedback(models.Model):
    customer=models.ForeignKey(Tbl_customer,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    msg=models.TextField(null=True)

    def __str__(self):
        return self.customer.first_name

