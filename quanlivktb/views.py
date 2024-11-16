from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import VuKhi, TrangBi, DonVi
from .forms import VuKhiForm, TrangBiForm

@login_required
def dashboard(request):
    context = {
        'total_vukhi': VuKhi.objects.count(),
        'total_trangbi': TrangBi.objects.count(),
        'don_vi': DonVi.objects.all()
    }
    return render(request, 'dashboard.html', context)

@login_required
def vukhi_list(request):
    vukhi = VuKhi.objects.select_related('don_vi').all()
    return render(request, 'vukhi.html', {'vukhi': vukhi})

@login_required
def trangbi_list(request):
    trangbi = TrangBi.objects.select_related('don_vi').all()
    return render(request, 'trangbi.html', {'trangbi': trangbi}) 