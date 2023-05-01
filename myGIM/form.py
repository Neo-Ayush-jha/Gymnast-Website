from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import *

class TrainerForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=('username','first_name','last_name','email',)
    def save(self,commit=True):
        user=super().save(commit=False)
        user.is_trainers=True
        if commit:
            user.save()
        return user
class PublicForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=User
        fields=('username','first_name','last_name','email',)
    def save(self,commit=True):
        user=super().save(commit=False)
        user.is_public=True
        if commit:
            user.save()
        return user
class ContactFrom(ModelForm):
    class Meta:
        model=Contact
        exclude=("user","timeStamp",)
class ContactTrainerFrom(ModelForm):
    class Meta:
        model=Trainer
        exclude=("user","timeStamp","isApproved",)
class FeedBackForm(ModelForm):
    class Meta:
        model=FeedBack
        exclude=("client","timeStamp",)