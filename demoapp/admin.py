from django.contrib import admin
from . models import User

class UserAdmin(admin.ModelAdmin):

    search_fields = ('date','first_name','email')

    list_display=('first_name','last_name','date','email','city')


admin.site.register(User,UserAdmin)