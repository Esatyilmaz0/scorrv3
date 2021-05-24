from django.contrib import admin
from import_export import resources
from .models import Log, RaporGirdiler, HamVeri, RaporReferanslari, SorguList
# Register your models here.
from import_export.admin import ImportExportModelAdmin

exclude_data = ("stok_tipi_1",
                    "stok_tipi_2",
                    "stok_tipi_3",
                    "stok_tipi_4",
                    "stok_tipi_5",
                    "stok_tipi_6",
                    "stok_tipi_7",
                    "stok_tipi_8",
                    "ekipman_no",
                    "teslim_alma_tarihi",
                    "sahaya_kurulum_tarihi",
                    "sirket",
                    "organization_code",
                    "department_code",
                    "ust_ekipman",
                    "kts_saha_no"
                    )

class HamVeriResource(resources.ModelResource):
    class Meta:
        model = HamVeri
        exclude = exclude_data
        batch_size = 100000000000

class HamVeriAdmin(ImportExportModelAdmin):
    list_display = ["saha_no", "saha_kodu"]
    resource_class = HamVeriResource
    exclude = exclude_data
    
class RaporReferanslariResource(resources.ModelResource):
    class Meta:
        model = RaporReferanslari
        exclude = ["grup_tanimi", "rapor_tanimi", "ref_grup", "kategori", "analiz_no"]

class RaporReferanslariAdmin(ImportExportModelAdmin):
    class Meta:
        resource_class = RaporReferanslariResource

class RaporGirdilerResource(resources.ModelResource):
    class Meta:
        model = RaporGirdiler
        
class RaporGirdilerAdmin(ImportExportModelAdmin):
    resource_class = RaporGirdilerResource
    list_display = ["id", "saha_no", "saha_kod", "aciklama"]
    search_fields = ["id"]
class SorguListResource(resources.ModelResource):
    class Meta:
        model = SorguList

class SorguListAdmin(ImportExportModelAdmin):
    class Meta:
        resource_class = SorguListResource

class LogAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "description", "created_at"]
    search_fields = ["id", "user"]
    list_filter = ["created_at"]
    
admin.site.register(SorguList, SorguListAdmin)

admin.site.register(RaporGirdiler, RaporGirdilerAdmin)

admin.site.register(RaporReferanslari, RaporReferanslariAdmin)

admin.site.register(HamVeri, HamVeriAdmin)

admin.site.register(Log, LogAdmin)