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
        return f"{self.madv} - ({self.tendv})"


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


class Hocvien(models.Model):
    mahv = models.CharField(max_length=255, primary_key=True)  
    madv = models.ForeignKey(DonVi, on_delete=models.CASCADE)  # Foreign key to DonVi
    tenhv = models.CharField(max_length=255)
    
    class Meta:        
        db_table = "hoc_vien"

    def __str__(self):
        return f"{self.mahv} - ({self.tenhv})"


class VuKhi(models.Model):
    LOAI_VU_KHI_CHOICES = [
        (0, 'Hoan Cai'),
        (1, 'SSCD'),
    ]

    masung = models.CharField(max_length=255, primary_key=True)
    makn = models.CharField(max_length=255)
    tenvk = models.TextField()
    loaivk = models.BooleanField(choices=LOAI_VU_KHI_CHOICES)  # Dùng choices để hiển thị "Hoan Cai" hoặc "SSCD"
    ghichu = models.TextField()

    class Meta:        
        db_table = "vu_khi"

    def __str__(self):
        return f"{self.tenvk} - {self.masung} - {self.makn} - {self.loaivk} - {self.ghichu}"


class TrangBi(models.Model):
    matb = models.CharField(max_length=255, primary_key=True)
    tentb = models.TextField()
    loai = models.TextField()
    tinhtrang = models.TextField()

    class Meta:        
        db_table = "trang_bi"

    def __str__(self):
        return f"{self.tentb} - {self.matb} - {self.loai} - {self.tinhtrang}"


class BienCheVuKhi(models.Model):
    mavk = models.ForeignKey(VuKhi, on_delete=models.CASCADE)  # Foreign key to VuKhi
    mahv = models.ForeignKey(Hocvien, on_delete=models.CASCADE)  # Foreign key to Hocvien
    madv = models.ForeignKey(DonVi, on_delete=models.CASCADE)  # Foreign key to DonVi

    class Meta:        
        db_table = "bien_che_vk"

    def __str__(self):
        return f"{self.mavk} - {self.mahv} - {self.madv}"


class BienCheTrangBi(models.Model):
    matb = models.ForeignKey(TrangBi, on_delete=models.CASCADE)  # Foreign key to TrangBi
    mahv = models.ForeignKey(Hocvien, on_delete=models.CASCADE)  # Foreign key to Hocvien
    madv = models.ForeignKey(DonVi, on_delete=models.CASCADE)  # Foreign key to DonVi

    class Meta:        
        db_table = "bien_che_tb"

    def __str__(self):
        return f"{self.matb} - {self.mahv} - {self.madv}"


class Thuoc(models.Model):
    madv = models.ForeignKey(DonVi, on_delete=models.CASCADE)  # Foreign key to DonVi
    username = models.ForeignKey(UserMod, on_delete=models.CASCADE)  # Foreign key to Hocvien
    

    class Meta:
        db_table = "thuoc"

    def __str__(self):
        return f"{self.macb} - {self.mahv} - {self.madv}"


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

class VuKhi(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='vukhi/', null=True)
    
    def __str__(self):
        return self.name

class TrangBi(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='trangbi/', null=True)
    
    def __str__(self):
        return self.name