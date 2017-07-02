from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import RxdUser, Profile

admin.site.register(RxdUser, UserAdmin)
admin.site.register(Profile)

class RxdUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_type', 'gender', 'birth_date', 'phone', 'city', 'job', 'college', 'description')
