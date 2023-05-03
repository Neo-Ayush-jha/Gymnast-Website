from django.db import models
from django.contrib.auth.models import AbstractUser
GENDER=(
    ("Mail","Mail"),
    ("Femail","Femail"),
    ("Other","Other"),
)
PLAN=(
    ("1-month > 3-month","1-month > 3-month"),
    ("4-month > 6-month","4-month > 6-month"),
    ("7-month > 12-month","7-month > 12-month"),
)
DAY=(
    ("Monday","Monday"),
    ("Tuesday","Tuesday"),
    ("Wednesday","Wednesday"),
    ("Thursday","Thursday"),
    ("Friday","Friday"),
    ("Saturday","Saturday"),
    ("Sunday","Sunday"),
)
TIME=(
    ("6:00am - 8:00am","6:00am - 8:00am"),
    ("8:00am - 10:00am","8:00am - 10:00am"),
    ("10:00am - 1:00pm","10:00am - 1:00pm"),
    ("1:00pm - 3:00pm","1:00pm - 3:00pm"),
    ("3:00pm - 5:00pm","3:00pm - 5:00pm"),
    ("5:00pm - 8:00pm","5:00pm - 8:00pm"),
    ("8:00pm - 10:00pm","8:00pm - 10:00pm"),
)
class User (AbstractUser):
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
    day=models.CharField(max_length=100,choices=DAY)
    time=models.CharField(max_length=100,choices=TIME)
    trainer=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    def __str__(self):
        return self.day + " - " + self.time +" - " + self.trainer.user.username
class FeedBack(models.Model):
    client=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField()
    timeStamp=models.DateTimeField(auto_created=True)
    def __str__(self):
        return self.client.username
class VideoClass(models.Model):
    pass

class Gallery(models.Model):
    topic=models.CharField(max_length=200)
    community=models.CharField(max_length=200)
    img=models.ImageField(upload_to="photo/" ,null=True,blank=True)
    def __str__(self) -> str:
        return self.topic
class Attendance(models.Model):
    selectdate=models.DateTimeField(auto_now=True)
    login=models.CharField(max_length=200)
    logout=models.CharField(max_length=200)
    selectWorkout=models.CharField(max_length=200)
    trainedBy=models.ForeignKey(Trainer,on_delete=models.CASCADE)