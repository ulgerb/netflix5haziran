from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from appUser.models import *

def profilePage(request):
   # ==================================

   profile_list = Profile.objects.filter(user=request.user)
   
   if request.method == "POST":
      submit = request.POST.get("submit")
      if submit == "profileCreate":
         title = request.POST.get("title")
         image = request.FILES.get("image")
         if title and image:
            if len(profile_list) < 4:
               profile = Profile(title=title, image=image, user= request.user)
               profile.save()
               return redirect("profilePage") # yönlendirme
            else:
               messages.error(request, "Çok Zorlama Kardeşim!!!")
         else:
            messages.error(request, "Boş bırakılan yerler var!!")
      elif submit == "profileDelete":
         profileid = request.POST.get("profileid")
         profile = Profile.objects.get(id=profileid)
         
         title = request.POST.get("title")
         image = request.FILES.get("image")

         profile.title = title
         if image:
            profile.image = image
         
         profile.save()
         return redirect("profilePage")
      
   context = {
      "profile_list":profile_list,
   }
   return render(request, 'profile.html', context)

def profileDelete(request, pid):
   profile = Profile.objects.get(id=pid)
   profile.delete()
   return redirect("profilePage")

def profileBrowse(request, pid):
   profile = Profile.objects.get(id=pid) # Giriş Yapılan Profile
   user_profile_list = Profile.objects.filter(user=request.user) # Kullanıcının Tüm Profilleri
   user_profile_list.update(islogin=False) # Tüm Profilleri Çıkış Yaptır.
   profile.islogin = True # Giriş Yapanı True Yap
   profile.save()
   return redirect("browsePage2")
   
   

def hesapPage(request):
   profile = Profile.objects.get(user=request.user, islogin=True)
   context = {
      "profile":profile
   }
   return render(request, 'hesap.html', context)

def videoPage(request):
   context = {}
   return render(request, 'video.html', context)

def loginPage(request):
   
   if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      remember = request.POST.get("rememberme")


      if remember:
         request.session.set_expiry(1209600)
      else:
         request.session.set_expiry(0)
         
      
      user = authenticate(username=username, password=password)
      if user is not None:
         login(request, user)
         messages.success(request, "Girişiniz Yapıldı...")
         return redirect("profilePage")
      else:
         messages.error(request, "Kullanıcı adı veya şifre yanlış!!")
         return redirect("loginPage")
         
   
   context = {}
   return render(request, 'user/login.html', context)

def registerPage(request):
   
   if request.method == "POST":
      fname = request.POST.get("fname")
      lname = request.POST.get("lname")
      email = request.POST.get("email")
      username = request.POST.get("username")
      password1 = request.POST.get("password1")
      password2 = request.POST.get("password2")
      check_site = request.POST.get("check-site")
      check_kvkk = request.POST.get("check-kvkk")

      if fname and lname and email and username and password1 and password2 and check_site and check_kvkk:
         if password1 == password2:
            if not User.objects.filter(username=username).exists():
               if not User.objects.filter(email=email).exists():

                  user = User.objects.create_user(username=username, password=password1, email=email,first_name=fname, last_name=lname )
                  user.save()
                  messages.success(request, "Kaydınız başarıyla oluşturuldu...")
                  return redirect("loginPage")
               else:
                  messages.error(request, "Bu email zaten kullanılıyor !!")
            else:
               messages.error(request, "Bu kullanıcı adı zaten kullanılıyor !!")
         else:
            messages.error(request, "Şifreler eşleşmiyor !!")
      else:
         messages.error(request, "Lütfen boş bırakılan yerleri doldurun !!")
                  
   context = {}
   return render(request, 'user/register.html', context)
