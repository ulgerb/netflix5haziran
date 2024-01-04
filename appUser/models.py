from django.db import models
from django.contrib.auth.models import User 
from django.utils.text import slugify

class Profile(models.Model):
   user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   title = models.CharField(("Profil Adı"), max_length=50)
   image = models.ImageField(("Profil Resmi"), upload_to="profile", max_length=200)
   islogin = models.BooleanField(("Profile Online mı?"), default=False)
   
   def __str__(self) -> str:
      return self.title + " " +self.user.username




class Packed(models.Model): 
   title = models.CharField(("Paket Adı"), max_length=50)
   price = models.FloatField(("Fiyat"))
   pre = models.BooleanField(("Premium Pakedi"), default=False)   
   spor = models.BooleanField(("Spor Pakedi"), default=False)   
   sinema = models.BooleanField(("Sinema Pakedi"), default=False)   
   slug = models.SlugField(("Slug"), blank=True)
   
   def __str__(self) -> str:
      return self.title
   
   def save(self):
      self.slug = slugify(self.title)
      super().save()
   

class Userinfo(models.Model):
   user = models.OneToOneField(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
   tel = models.CharField(("Telefon"), max_length=50, default="-")
   address = models.TextField(("Adres"), default="-", blank=True)
   packed = models.ForeignKey(Packed, verbose_name=("Pakedi"), on_delete=models.CASCADE)
   
   def __str__(self) -> str:
      return self.user.username