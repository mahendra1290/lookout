from django.contrib import admin

from .models import List, User

admin.site.register(User)
admin.site.register(List)
# Register your models here.
