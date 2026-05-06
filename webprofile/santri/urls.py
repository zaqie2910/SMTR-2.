from django.urls import path
from . import views

urlpatterns = [
    path("", views.santri_home, name="santri_home"),
    path("biodata/", views.biodata, name="biodata"),
    path("jadwal/", views.jadwal, name="jadwal"),
    path("galeri/", views.galeri, name="galeri"),
    path("feedback/", views.feedback, name="feedback"),
# Kegunaan: Buat halaman SANGAT Sederhana yang GAK BUTUH logic apapun
# Gak perlu bikin file views.py
# Langsung di URL
# Cocok buat: homepage statis, about, terms

]