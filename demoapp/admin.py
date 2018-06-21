from django.contrib import admin
from . models import User

class UserAdmin(admin.ModelAdmin):

    search_fields = ('date','first_name','email','city','user_id')
    list_display=('first_name','last_name','date','email','city')

admin.site.register(User,UserAdmin)