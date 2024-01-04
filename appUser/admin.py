from django.contrib import admin
from appUser.models import *

# adminview
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

   list_display = ('user','title', 'islogin')
   search_fields = ('title','user__username')
   
   
@admin.register(Packed)
class PackedAdmin(admin.ModelAdmin):

   list_display = ('title', 'price','pre','spor','sinema','slug')
 
   
@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):

   list_display = ('user','tel', 'packed')

