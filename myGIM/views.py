from django.shortcuts import render,redirect,HttpResponse
from .form import * 
from .models import *
from .decorators import *
from django.views.generic import CreateView,View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login , logout ,authenticate
from django.utils import timezone
from datetime import datetime

def home(req):
    return render(req,"index.html")
def classes(req):
    return render(req,"class.html")
def aboutUs(req):
    data={
        'traner':Trainer.objects.filter(isApproved=True),
    }
    return render(req,"about.html",data)
def feature(req):
    data={'fedback':FeedBack.objects.all(),}
    return render(req,"feature.html",data)
class TrainerSingup(CreateView):
    model = User
    form_class=TrainerForm
    template_name="singup.html"
    success_url="/"
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = "Trainer"
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")
class PublicSingup(CreateView):
    model = User
    form_class=PublicForm
    template_name="singup.html"
    success_url="/"
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = "Public"
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")
class Logout(View):
    def get(self,req):
        logout(req)
        return redirect(home)
def Login(request):
    form_class=AuthenticationForm(data=request.POST or None)
    if request.method =="POST":
        if form_class.is_valid():
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    back=request.GET.get("next","/")
                    return redirect(back)
                else:
                    return HttpResponse("Inactivated")
            else:
                return HttpResponse("login cheeking is failed")
    return render(request,"login.html",{"form":form_class})
@login_required
def join(req):
    user=User.objects.get(pk=req.user.id)
    selectTrainer=Trainer.objects.filter(isApproved=True)
    form=ContactFrom
    plan=MembershipPlan.objects.all()
    currentMonth=datetime.now()

    if req.method=="POST":
        selectTrainer=req.POST.get('selectTrainer')
        plan=req.POST.get('plan')

        form=Contact()
        form.user=user
        form.description=req.POST.get('description')
        form.reference=req.POST.get('reference')
        form.address=req.POST.get('address')
        form.DOB=req.POST.get('DOB')
        form.gender=req.POST.get('gender')
        form.phoneNumber=req.POST.get('phoneNumber')
        form.profile_Picture=req.FILES.get('profile_Picture')
        form.timeStamp=currentMonth
        form.plan=MembershipPlan.objects.get(pk=plan)
        form.selectTrainer=Trainer.objects.get(pk=selectTrainer)
        print(form.selectTrainer)
        form.save()
        return redirect(home)
    data={'form':form,'selectTrainer':selectTrainer,'plan':plan}
    return render(req,"join.html",data)

@login_required
def joinASTrainer(req):
    user=User.objects.get(pk=req.user.id)
    form=ContactTrainerFrom
    currentMonth=datetime.now()

    if req.method=="POST":
        form=Trainer()
        form.user=user
        form.address=req.POST.get('address')
        form.DOB=req.POST.get('DOB')
        form.gender=req.POST.get('gender')
        form.phoneNumber=req.POST.get('phoneNumber')
        form.salary=req.POST.get('salary')
        form.profile_Picture=req.FILES.get('profile_Picture')
        form.timeStamp=currentMonth

        form.save()
        return redirect(home)
    return render(req,"joinASTrainer.html",{"form":form})
@login_required
def feedBack(req):
    client=User.objects.get(pk=req.user.id)
    form=FeedBackForm
    currentMonth=datetime.now()

    if req.method=="POST":
        form=FeedBack()
        form.client=client
        form.message=req.POST.get('message')
        form.timeStamp=currentMonth
        form.save()
        return redirect(home)
    return render(req,"feedback.html",{'form':form})