from django.contrib import admin
from .models import Position, Worker
from django_mptt_admin.admin import DjangoMpttAdmin


admin.site.register(Position)
admin.site.register(Worker)