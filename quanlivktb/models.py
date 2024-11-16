from django.db import models
from django.contrib.auth.models import User

class DonVi(models.Model):
    ma_dv = models.CharField(max_length=10, primary_key=True)
    ten_dv = models.CharField(max_length=100)
    dia_chi = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'donvi'

class VuKhi(models.Model):
    ma_vk = models.CharField(max_length=10, primary_key=True)
    ten_vk = models.CharField(max_length=100)
    so_luong = models.IntegerField()
    tinh_trang = models.CharField(max_length=50)
    don_vi = models.ForeignKey(DonVi, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'vukhi'

class TrangBi(models.Model):
    ma_tb = models.CharField(max_length=10, primary_key=True)
    ten_tb = models.CharField(max_length=100)
    so_luong = models.IntegerField()
    tinh_trang = models.CharField(max_length=50)
    don_vi = models.ForeignKey(DonVi, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'trangbi' 