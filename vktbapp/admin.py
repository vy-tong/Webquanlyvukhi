from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserMod, DonVi, Hocvien, VuKhi, TrangBi, BienCheVuKhi, BienCheTrangBi, Thuoc
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserMod
    list_display = ['username', 'email', 'is_canbo', 'is_hocvien']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'avatar', 'is_canbo', 'is_hocvien')}),
    )

admin.site.register(UserMod, CustomUserAdmin)

# Đăng ký model DonVi
@admin.register(DonVi)
class DonViAdmin(admin.ModelAdmin):
    list_display = ('madv', 'tendv')
    search_fields = ('madv', 'tendv')

# Đăng ký model Hocvien
@admin.register(Hocvien)
class HocvienAdmin(admin.ModelAdmin):
    list_display = ('mahv', 'tenhv', 'madv')
    search_fields = ('mahv', 'tenhv')
    list_filter = ('madv',)

# Đăng ký model VuKhi
@admin.register(VuKhi)
class VuKhiAdmin(admin.ModelAdmin):
    list_display = ('masung', 'makn', 'tenvk', 'loaivk', 'ghichu')
    search_fields = ('masung', 'tenvk')
    list_filter = ('loaivk',)

# Đăng ký model TrangBi
@admin.register(TrangBi)
class TrangBiAdmin(admin.ModelAdmin):
    list_display = ('matb', 'tentb', 'loai', 'tinhtrang')
    search_fields = ('matb', 'tentb')
    list_filter = ('loai', 'tinhtrang')

# Đăng ký model BienCheVuKhi
@admin.register(BienCheVuKhi)
class BienCheVuKhiAdmin(admin.ModelAdmin):
    list_display = ('mavk', 'mahv', 'madv')
    search_fields = ('mavk', 'mahv')
    list_filter = ('madv',)

# Đăng ký model BienCheTrangBi
@admin.register(BienCheTrangBi)
class BienCheTrangBiAdmin(admin.ModelAdmin):
    list_display = ('matb', 'mahv', 'madv')
    search_fields = ('matb', 'mahv')
    list_filter = ('madv',)

# Đăng ký model Thuoc
@admin.register(Thuoc)
class ThuocAdmin(admin.ModelAdmin):
    list_display = ('madv', 'username')
    search_fields = ('madv', 'username')
    list_filter = ('madv',)