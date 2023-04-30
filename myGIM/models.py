from django.db import models
from django.contrib.auth.models import AbstractUser
GENDER=(
    ("Mail","Mail"),
    ("Femail","Femail"),
    ("Other","Other"),
)
PLAN=(
    ("3-month","3-month"),
    ("6-month","6-month"),
    ("12-month","12-month"),
)
class User(AbstractUser):
    is_trainers=models.BooleanField(default=False)
    is_public=models.BooleanField(default=False)

class MembershipPlan(models.Model):
    plan=models.CharField(max_length=20,choices=PLAN)
    price=models.IntegerField()
    def __str__(self) -> str:
        return self.plan
class Trainer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_Picture=models.ImageField(upload_to="photo/" ,null=True,blank=True)
    address=models.TextField(help_text="line1,city,state,pincode")
    DOB=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=20,choices=GENDER,default=None,null=True,blank=True)
    phoneNumber=models.IntegerField(null=True,blank=True)
    salary=models.IntegerField(default=None,null=True,blank=True)
    timeStamp=models.DateTimeField(auto_created=True)
    isApproved=models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
class Contact(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_Picture=models.ImageField(upload_to="photo/" ,null=True,blank=True)
    address=models.TextField(help_text="line1,city,state,pincode")
    DOB=models.DateField(null=True,blank=True)
    gender=models.CharField(max_length=20,choices=GENDER,default=None,null=True,blank=True)
    phoneNumber=models.IntegerField(null=True,blank=True)
    description=models.TextField()
    plan=models.ForeignKey(MembershipPlan,on_delete=models.CASCADE)
    reference=models.CharField(max_length=150)
    selectTrainer=models.ForeignKey(Trainer,on_delete=models.CASCADE,default=False,null=True,blank=True)
    timeStamp=models.DateTimeField(auto_created=True)
    def __str__(self):
        return self.user.username
class TimeTable(models.Model):
    pass
class FeedBack(models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField()
    timeStamp=models.DateTimeField(auto_created=True)
    def __str__(self):
        return self.client.username
class VideoClass(models.Model):
    pass