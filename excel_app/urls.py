from django.urls import path
from .views import about, contact, home, rapor_getir, raporlariGetir, updateAciklama, SignUpView, uploadHamVeri, CustomLoginView

urlpatterns = [
    path('', home),
    path('rapor_getir/', rapor_getir),
    path("updateAciklama/", updateAciklama),
    path('register/', SignUpView.as_view()),
    path('raporlar/', uploadHamVeri),
    path('login/', CustomLoginView.as_view(), name='login'),
    path("hakkimizda/", about),
    path("iletisim/", contact),
    path("raporlari_getir", raporlariGetir)
]