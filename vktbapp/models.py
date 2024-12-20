from django.db import models
from django.contrib.auth.models import AbstractUser

class UserMod(AbstractUser):
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)

class DonVi(models.Model):
    ma_dv = models.CharField(max_length=10, primary_key=True)
    ten_dv = models.CharField(max_length=100)
    dia_chi = models.CharField(max_length=200)
    
    def __str__(self):
        return self.ten_dv

class VuKhi(models.Model):
    ma_vk = models.CharField(max_length=10, primary_key=True)
    ten_vk = models.CharField(max_length=100)
    so_luong = models.IntegerField()
    tinh_trang = models.CharField(max_length=50)
    don_vi = models.ForeignKey(DonVi, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ten_vk

class TrangBi(models.Model):
    ma_tb = models.CharField(max_length=10, primary_key=True)
    ten_tb = models.CharField(max_length=100)
    so_luong = models.IntegerField()
    tinh_trang = models.CharField(max_length=50)
    don_vi = models.ForeignKey(DonVi, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ten_tb