from django.contrib import admin

# Register your models here.
from .models import profile


# class profileAdmin(admin.Modeladmin):

#     class Meta:
#         model = profile
admin.site.register(profile)
