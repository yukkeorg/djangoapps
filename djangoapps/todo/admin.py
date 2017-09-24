from django.contrib import admin

from .models import Todo, Expire, Done

# Register your models here.
admin.site.register(Todo)
admin.site.register(Expire)
admin.site.register(Done)
