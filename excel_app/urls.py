from django.urls import path
from django.urls.conf import include
from .views import bakimEnvanterGirdiUpdate, bakimRaporOlustur, kontrolRaporOlustur, permissionDenied, raporEnvanterUpdate, raporHatali, raporOnayla, satirEkle, sayimSonucRaporuOlustur, sendMailKontrolRapor, sendMailRapor, updateAciklama, SignUpView, CustomLoginView, clear
from django.contrib.auth import views
urlpatterns = [
    path('', CustomLoginView.as_view()),
    path("updateAciklama/", updateAciklama),
    path('register/', SignUpView.as_view()),
    path('bakimRapor/', bakimRaporOlustur),
    path('login/', CustomLoginView.as_view(), name='login'),
    
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('accounts/', include('django.contrib.auth.urls')),
    path("clear/<str:param>", clear),
    path("kontroleGonder/", sendMailRapor),
    path("updateSayimSonrasiGirdi/", bakimEnvanterGirdiUpdate),
    path("sayimSonucRaporuOlustur/", sayimSonucRaporuOlustur),
    
    path("raporOnayla/", raporOnayla),
    path("raporHatali/", raporHatali),
    
    path("kontrolRaporlar/", kontrolRaporOlustur),
    
    
    path('raporEmaille/', sendMailKontrolRapor),
    path("satirEkle/", satirEkle),
    path("raporEnvanterUpdate/", raporEnvanterUpdate),
    path("permissionDenied/", permissionDenied)
]