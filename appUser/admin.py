from django.contrib import admin
from appUser.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# adminview
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

   list_display = ('user','title', 'islogin')
   search_fields = ('title','user__username')
   
   
@admin.register(Packed)
class PackedAdmin(admin.ModelAdmin):

   list_display = ('title', 'price','pre','spor','sinema','slug')
 
   
# @admin.register(Userinfo)
# class UserinfoAdmin(admin.ModelAdmin):

#    list_display = ('user','tel', 'packed')


class UsermyInline(admin.StackedInline):
   model = Usermy
   max_num = 1
   can_delete = False
   
class CustomUser(UserAdmin):
   inlines = [UsermyInline,]
   
admin.site.unregister(User)
admin.site.register(User, CustomUser)