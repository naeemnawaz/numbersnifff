from django.contrib import admin
from django import forms




# Register your models here.
from myapp.models import Contact
admin.site.register(Contact)




from myapp.models import Subscribers
admin.site.register(Subscribers)

