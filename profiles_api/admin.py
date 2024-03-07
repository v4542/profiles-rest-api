from django.contrib import admin
from profiles_api import models

admin.site.register(models.UserProfile)#This tells the Django admin to register our user profile model with the admin site so it makes accessible through the admin interface
