from django.db import models

from django.contrib.auth.models import AbstractUser
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone

class DonVi(models.Model):
    madv = models.CharField(max_length=255, primary_key=True)
    tendv = models.TextField()

    class Meta:        
        db_table = "don_vi"

    def __str__(self):
        return self.tendv  # Changed from tentb to tendv


class UserMod(AbstractUser):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'}, 
                              help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                              max_length=150, 
                              unique=True,
                              validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                              verbose_name='username')
    email = models.EmailField(blank=True, max_length=254, verbose_name='email address')
    phone = models.CharField(max_length=20, null=True)
    avatar = models.ImageField(upload_to='avatars/', null=True)
    is_canbo = models.BooleanField(default=False, 
                                 help_text='Designates whether the user can log into this admin site.',
                                 verbose_name='staff status')
    is_hocvien = models.BooleanField(default=False)
    
    class Meta:
        db_table = "Tai_khoan"
        
    def __str__(self):
        return self.username


class VuKhi(models.Model):
    mavk = models.CharField(max_length=10, primary_key=True)
    makn = models.CharField(max_length=10)
    tenvk = models.CharField(max_length=100)
    loaivk = models.CharField(max_length=50)
    ghichu = models.TextField(blank=True, null=True)

    class Meta:        
        db_table = "vu_khi"

    def __str__(self):
        return self.tenvk


class TrangBi(models.Model):
    matb = models.CharField(max_length=10, primary_key=True)
    tentb = models.CharField(max_length=100)
    loai = models.CharField(max_length=50)
    tinhtrang = models.CharField(max_length=50)

    class Meta:        
        db_table = "trang_bi"

    def __str__(self):
        return self.tentb


class BienCheVuKhi(models.Model):
    mavk = models.ForeignKey(VuKhi, on_delete=models.CASCADE)
    mahv = models.ForeignKey('Hocvien', on_delete=models.CASCADE)
    madv = models.ForeignKey(DonVi, on_delete=models.CASCADE)

    class Meta:        
        db_table = "bien_che_vk"

    def __str__(self):
        return f"{self.mavk} - {self.mahv} - {self.madv}"


class BienCheTrangBi(models.Model):
    matb = models.ForeignKey(TrangBi, on_delete=models.CASCADE)
    mahv = models.ForeignKey('Hocvien', on_delete=models.CASCADE)
    madv = models.ForeignKey(DonVi, on_delete=models.CASCADE)

    class Meta:        
        db_table = "bien_che_tb"

    def __str__(self):
        return f"{self.matb} - {self.mahv} - {self.madv}"


class Thuoc(models.Model):
    madv = models.ForeignKey(DonVi, on_delete=models.CASCADE)
    username = models.ForeignKey(UserMod, on_delete=models.CASCADE)
    

    class Meta:
        db_table = "thuoc"

    def __str__(self):
        return f"{self.macb} - {self.mahv} - {self.madv}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name