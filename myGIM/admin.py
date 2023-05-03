from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Trainer)
admin.site.register(MembershipPlan)
admin.site.register(FeedBack)
admin.site.register(TimeTable)
admin.site.register(Gallery)
admin.site.register(Attendance)