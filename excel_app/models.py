from django.db import models

# Create your models here.

class SorguList(models.Model):
    sorgu_no = models.CharField(verbose_name="Sorgu No", max_length=5000)
    kontrol = models.CharField(verbose_name="Kontrol", max_length=5000)
    ref_grup = models.CharField(verbose_name="Ref Grup", max_length=5000)
    kategori = models.CharField(verbose_name="Kategori", max_length=5000)
    check = models.CharField(verbose_name="Check", max_length=5000)

class HamVeri(models.Model):
    saha_no = models.CharField(verbose_name="Saha No", max_length=50)
    saha_kodu = models.CharField(verbose_name="Saha Kod", max_length=50)
    kts_saha_no = models.CharField(verbose_name="KTS Saha No", max_length=50, default="")
    saha_tipi = models.CharField(verbose_name="Saha Tipi", max_length=5000)
    ana_yer_tipi = models.CharField(verbose_name="Ana Yer Tipi", max_length=5000)
    ekipman_no = models.CharField(verbose_name="Ekipman No", max_length=5000)
    ekipman_seri_no = models.CharField(verbose_name="Ekipman Seri No", max_length=5000, default="")
    ekipman_parca_kodu = models.CharField(verbose_name="Ekipman Parça Kodu", max_length=5000)
    parca_tanimi = models.CharField(verbose_name="Parça Tanımı", max_length=5000)
    stok_tipi_1 = models.CharField(verbose_name="Stok Tipi-1", max_length=5000)
    stok_tipi_2 = models.CharField(verbose_name="Stok Tipi-2", max_length=5000)
    stok_tipi_3 = models.CharField(verbose_name="Stok Tipi-3", max_length=5000)
    stok_tipi_4 = models.CharField(verbose_name="Stok Tipi-4", max_length=5000)
    stok_tipi_5 = models.CharField(verbose_name="Stok Tipi-5", max_length=5000)
    stok_tipi_6 = models.CharField(verbose_name="Stok Tipi-6", max_length=5000)
    stok_tipi_7 = models.CharField(verbose_name="Stok Tipi-7", max_length=5000)
    stok_tipi_8 = models.CharField(verbose_name="Stok Tipi-8", max_length=5000)
    teslim_alma_tarihi = models.CharField(verbose_name="Teslim Alma Tarihi", max_length=5000)
    sahaya_kurulum_tarihi = models.CharField(verbose_name="Sahaya Kurulum Tarihi", max_length=5000)
    sirket = models.CharField(verbose_name="Şirket", max_length=5000)
    organization_code = models.CharField(verbose_name="Organization Code", max_length=5000)
    department_code = models.CharField(verbose_name="Department", max_length=5000)
    quantity = models.IntegerField(verbose_name="Quantity")
    ust_ekipman = models.CharField(verbose_name="Üst Ekipman", max_length=5000, default="")
    
    
class RaporReferanslari(models.Model):
    
    sorgu_no = models.CharField(verbose_name="Sorgu No", max_length=5000)
    ref = models.CharField(verbose_name="Ref", max_length=5000)
    ekipman_parca_kodu = models.CharField(verbose_name="Ekipman Parça Kodu", max_length=5000)
    parca_tanimi = models.CharField(verbose_name="Parça Tanımı", max_length=5000)
    grup_tanimi = models.CharField(verbose_name="Grup Tanımı", max_length=5000)
    rapor_tanimi = models.CharField(verbose_name="Rapor Tanımı", max_length=5000)
    ref_grup = models.CharField(verbose_name="Ref Grup", max_length=5000)
    kategori = models.CharField(verbose_name="Kategori", max_length=5000)
    analiz_no = models.CharField(verbose_name="Analiz No", max_length=5000)

class RaporGirdiler(models.Model):
    saha_no = models.CharField(verbose_name="Saha No", max_length=50)
    saha_kod = models.CharField(verbose_name="Saha Kod", max_length=50)
    ref_1 = models.IntegerField(verbose_name="Referans-1")
    ref_2 = models.IntegerField(verbose_name="Referans-2")
    ref_3 = models.IntegerField(verbose_name="Referans-3")
    ref_4 = models.IntegerField(verbose_name="Referans-4")
    ref_5 = models.IntegerField(verbose_name="Referans-5")
    ref_6 = models.IntegerField(verbose_name="Referans-6")
    ref_grup = models.CharField(verbose_name="Ref Grup", max_length=5000)
    sonuc = models.CharField(verbose_name="Sonuç", max_length=50)
    kontrol = models.CharField(verbose_name="Kontrol", max_length=5000)
    kategori = models.CharField(verbose_name="Kategori", max_length=50)
    sorgu_no = models.CharField(verbose_name="Sorgu No", max_length=50)
    aciklama = models.CharField(verbose_name="Açıklama", max_length=5000,blank=True,null=False, default="")
    
    def __str__(self) -> str:
        return self.kontrol
    
class Log(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Kullanıcı")
    description = models.TextField(verbose_name="Yaptığı İşlem", max_length=9999999)
    created_at = models.DateTimeField(verbose_name="Oluşturulma Tarihi", auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user.username
    

    