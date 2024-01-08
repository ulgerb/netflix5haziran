from django.shortcuts import render, redirect
from appUser.models import Profile
from django.contrib import messages
from django.core.mail import send_mail
from netflix5haziran.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User

def indexPage(request):
   context = {}
   return render(request, 'index.html', context)

def browsePage(request, pid=None):
   if pid:
      profile = Profile.objects.get(id=pid)
   else:
      profile = Profile.objects.get(user=request.user, islogin=True)
   context = {
      "profile":profile,
   }
   return render(request, 'browse-index.html', context)

def emailSendPage(request):

   users = User.objects.all().values("email")
   # print(list(users)) # [{'email': 'basriberkay2@gmail.com'}, {'email': 'aaa@aaa.com'}, {'email': ''}]
   user_list = []
   for i in list(users):
      user_list.append(i["email"])
   
   if request.method == "POST":
      title = request.POST.get("title")
      text = request.POST.get("text")
      try:
         send_mail(
            title,
            text,
            EMAIL_HOST_USER,
            user_list,
            fail_silently=False,
         )
         messages.success(request, "Mesajlar Başarıyla Gönderildi. ")
      except:
         messages.error(request, "Mesaj Gönderilemedi")
   
      return redirect("emailSendPage")
   
   context = {}
   return render( request, "email-send.html", context)
