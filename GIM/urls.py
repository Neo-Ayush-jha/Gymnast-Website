from django.contrib import admin
from django.urls import path
from myGIM.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home,name='home'),
    path("about/",aboutUs,name='about'),
    path("classes/",classes,name='classes'),
    path("our/feature/",feature,name='feature'),
    path("singup/as-trainer/",TrainerSingup.as_view(),name="singup_trainer"),
    path("singup/as-public/",PublicSingup.as_view(),name="singup_public"),
    path("logout/",Logout.as_view(),name="logout"),
    path("login/",Login,name="login"),
    path("enrollment/",join,name="join"),
    path("feedback/",feedBack,name="feedBack"),
    path("join/as/trainer/",joinASTrainer,name="joinASTrainer"),
    path("single/view/",singleView,name="singleView"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)