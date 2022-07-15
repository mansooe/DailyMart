from django.contrib import admin
from userapp.models import ContactusDb, UserDb
# Register your models here.
admin.site.register(UserDb)
admin.site.register(ContactusDb)