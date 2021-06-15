from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.db.models.fields import related
from django.dispatch import receiver
User._meta.get_field('email')._unique = True

# Create your models here.
class Departmanlar(models.Model):
    code = models.CharField(verbose_name="Departman Kodu", max_length=9999)
    emails = models.TextField(verbose_name="Email Listesi", help_text="Mailleri Her Satıra Bir Tane Gelecek Şekilde Yazın")
    def __str__(self):
        return self.code
   
class Rapor(models.Model):
    user = models.ForeignKey("auth.User", related_name="raporlar", on_delete=models.SET_NULL, null=True, blank=True)
    saha_no = models.CharField(verbose_name="Saha No", max_length=9999, default="")
    saha_kod = models.CharField(verbose_name="Saha Kodu", max_length=9999, default="")
    created_at = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    department_code = models.ForeignKey(Departmanlar, on_delete=models.SET_DEFAULT, default="", null=True, blank=True)
    onay = models.BooleanField(verbose_name="Rapor Onaylı'mı?", default=False)
    child = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)
    hatali = models.BooleanField(verbose_name="Hatalı mı?", default=False)
    def __str__(self):
        return f"{self.saha_no} Saha No'suna Ait {self.id} ID'li Rapor"
    

    


class SorguList(models.Model):
    sorgu_no = models.CharField(verbose_name="Sorgu No", max_length=5000, default="")
    kontrol = models.CharField(verbose_name="Kontrol", max_length=5000, default="")
    ref_grup = models.CharField(verbose_name="Ref Grup", max_length=5000, default="")
    kategori = models.CharField(verbose_name="Kategori", max_length=5000, default="")
    check = models.CharField(verbose_name="Check", max_length=5000, default="")

class SayimOncesiEnvanter(models.Model):
    saha_no = models.CharField(verbose_name="Saha No", max_length=50, default="")
    saha_kodu = models.CharField(verbose_name="Saha Kod", max_length=50, default="")
    kts_saha_no = models.CharField(verbose_name="KTS Saha No", max_length=50, default="")
    saha_tipi = models.CharField(verbose_name="Saha Tipi", max_length=5000, default="")
    ana_yer_tipi = models.CharField(verbose_name="Ana Yer Tipi", max_length=5000, default="")
    ekipman_no = models.CharField(verbose_name="Ekipman No", max_length=5000, default="")
    ekipman_seri_no = models.CharField(verbose_name="Ekipman Seri No", max_length=5000, default="")
    ekipman_parca_kodu = models.CharField(verbose_name="Ekipman Parça Kodu", max_length=5000, default="")
    parca_tanimi = models.CharField(verbose_name="Parça Tanımı", max_length=5000, default="")
    stok_tipi_1 = models.CharField(verbose_name="Stok Tipi-1", max_length=5000, default="")
    stok_tipi_2 = models.CharField(verbose_name="Stok Tipi-2", max_length=5000, default="")
    stok_tipi_3 = models.CharField(verbose_name="Stok Tipi-3", max_length=5000, default="")
    stok_tipi_4 = models.CharField(verbose_name="Stok Tipi-4", max_length=5000, default="")
    stok_tipi_5 = models.CharField(verbose_name="Stok Tipi-5", max_length=5000, default="")
    stok_tipi_6 = models.CharField(verbose_name="Stok Tipi-6", max_length=5000, default="")
    stok_tipi_7 = models.CharField(verbose_name="Stok Tipi-7", max_length=5000, default="")
    stok_tipi_8 = models.CharField(verbose_name="Stok Tipi-8", max_length=5000, default="")
    teslim_alma_tarihi = models.CharField(verbose_name="Teslim Alma Tarihi", max_length=5000, default="")
    sahaya_kurulum_tarihi = models.CharField(verbose_name="Sahaya Kurulum Tarihi", max_length=5000, default="")
    sirket = models.CharField(verbose_name="Şirket", max_length=5000, default="")
    organization_code = models.CharField(verbose_name="Organization Code", max_length=5000, default="")
    department_code = models.CharField(verbose_name="Department", max_length=5000, default="")
    quantity = models.IntegerField(verbose_name="Quantity", default=0)
    ust_ekipman = models.CharField(verbose_name="Üst Ekipman", max_length=5000, default="")
    rapor = models.ForeignKey(Rapor, on_delete=models.CASCADE, default="")
    
class SayimSonrasiEnvanter(models.Model):
    saha_no = models.CharField(verbose_name="Saha No", max_length=50, default="")
    saha_kodu = models.CharField(verbose_name="Saha Kod", max_length=50, default="")
    ekipman_seri_no = models.CharField(verbose_name="Ekipman Seri No", max_length=5000, default="")
    ekipman_parca_kodu = models.CharField(verbose_name="Ekipman Parça Kodu", max_length=5000, default="")
    parca_tanimi = models.CharField(verbose_name="Parça Tanımı", max_length=5000, default="")
    department_code = models.CharField(verbose_name="Department", max_length=5000, default="")
    quantity = models.IntegerField(verbose_name="Quantity", default="")
    aciklama = models.CharField(verbose_name="Açıklama", max_length=5000, default="")
    sayim = models.IntegerField(verbose_name="Sayim", default=0)
    rapor = models.ForeignKey(Rapor, on_delete=models.CASCADE, related_name="sayim_sonrasi_envanter")
    
class RaporReferanslari(models.Model):

    sorgu_no = models.CharField(verbose_name="Sorgu No", max_length=5000, default="")
    ref = models.CharField(verbose_name="Ref", max_length=5000, default="")
    ekipman_parca_kodu = models.CharField(verbose_name="Ekipman Parça Kodu", max_length=5000, default="")
    parca_tanimi = models.CharField(verbose_name="Parça Tanımı", max_length=5000, default="")
    grup_tanimi = models.CharField(verbose_name="Grup Tanımı", max_length=5000, default="")
    rapor_tanimi = models.CharField(verbose_name="Rapor Tanımı", max_length=5000, default="")
    ref_grup = models.CharField(verbose_name="Ref Grup", max_length=5000, default="")
    kategori = models.CharField(verbose_name="Kategori", max_length=5000, default="")
    analiz_no = models.CharField(verbose_name="Analiz No", max_length=5000, default="")

class SayimRapor(models.Model):
    saha_no = models.CharField(verbose_name="Saha No", max_length=50, default="")
    saha_kod = models.CharField(verbose_name="Saha Kod", max_length=50, default="")
    ref_1 = models.IntegerField(verbose_name="Referans-1")
    ref_2 = models.IntegerField(verbose_name="Referans-2")
    ref_3 = models.IntegerField(verbose_name="Referans-3")
    ref_4 = models.IntegerField(verbose_name="Referans-4")
    ref_5 = models.IntegerField(verbose_name="Referans-5")
    ref_6 = models.IntegerField(verbose_name="Referans-6")
    ref_grup = models.CharField(verbose_name="Ref Grup", max_length=5000, default="")
    sonuc = models.CharField(verbose_name="Sonuç", max_length=50, default="")
    kontrol = models.CharField(verbose_name="Kontrol", max_length=5000, default="")
    kategori = models.CharField(verbose_name="Kategori", max_length=50, default="")
    sorgu_no = models.CharField(verbose_name="Sorgu No", max_length=50, default="")
    aciklama = models.CharField(verbose_name="Açıklama", max_length=5000,blank=True,null=False, default="")
    rapor = models.ForeignKey(Rapor, related_name="girdiler", on_delete=models.CASCADE)
    
    is_sayim_sonrasi = models.BooleanField(verbose_name="Sayım Sonrası Girdisi Mi?", default=False)
    created_at = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    def __str__(self):
        return self.kontrol

class Log(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Kullanıcı")
    saha_no = models.CharField(verbose_name="Saha No", max_length=50, default="")
    saha_kod = models.CharField(verbose_name="Saha Kod", max_length=50, default="")

    description = models.TextField(verbose_name="Yaptığı İşlem", max_length=9999999, default="")
    created_at = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)

    def __str__(self):
        return self.user.username


class RaporEnvanter(models.Model):
    saha_no = models.CharField(verbose_name="Saha No", max_length=50, default="")
    user = models.CharField(verbose_name="Kullanıcı Adı", max_length=50, default="")
    seri_no = models.CharField(verbose_name="Seri No", max_length=5000, default="")
    parca_kodu = models.CharField(verbose_name="Parça Kodu", max_length=5000, default="")
    parca_tanimi = models.CharField(verbose_name="Parça Tanımı", max_length=5000, default="")
    bolge = models.CharField(verbose_name="Bölge", max_length=5000, default="")
    miktar = models.IntegerField(verbose_name="Miktar", default=0)
    sayim_fark = models.IntegerField(verbose_name="Sayım Fark", default=0)
    transfer_adet = models.IntegerField(verbose_name="Transfer Adet", default=0)
    sonuc = models.CharField(verbose_name="Sonuç", max_length=9999, default="")
    durum = models.CharField(verbose_name="Durum", max_length=9999, default="")
    lokasyon = models.CharField(verbose_name="Lokasyon", max_length=9999, default="")
    aciklama = models.CharField(verbose_name="Açıklama", max_length=99999, default="")
    rapor = models.ForeignKey(Rapor, on_delete=models.CASCADE, related_name="rapor_envanter")
    
class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE, related_name="profile")
    department_code = models.CharField(verbose_name="Departman Kodu", max_length=50)
    kontrolcu = models.BooleanField(verbose_name="Kontrolcü", default=False)
    bakimci = models.BooleanField(verbose_name="Bakımcı", default=False)
    denetci = models.BooleanField(verbose_name="Denetçi", default=False)
    def __str__(self):
        return self.user.username or self.user.email

@receiver(signals.post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    
