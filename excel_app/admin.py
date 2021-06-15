from django.contrib import admin
from import_export import resources
from .models import Departmanlar, Log, Rapor, RaporEnvanter, SayimRapor, SayimOncesiEnvanter, RaporReferanslari, SayimSonrasiEnvanter, SorguList, UserProfile
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
        model = SayimOncesiEnvanter
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
    change_list_template = "admin/clear_referans.html"
    list_display = ["id", "sorgu_no", "ref", "ekipman_parca_kodu", "parca_tanimi"]
    class Meta:
        resource_class = RaporReferanslariResource

class RaporGirdilerResource(resources.ModelResource):
    class Meta:
        model = SayimRapor

class RaporGirdilerAdmin(ImportExportModelAdmin):
    list_display = ["id", "saha_no", "saha_kod", "aciklama"]
    search_fields = ["id"]
    class Meta:
        resource_class = RaporGirdilerResource


class RaporResource(resources.ModelResource):
    class Meta:
        model = Rapor

class RaporAdmin(ImportExportModelAdmin):
    list_display = ["id", "saha_no", "saha_kod", "user", "department_code"]
    search_fields = ["id"]
    class Meta:
        resource_class = RaporResource

class SorguListResource(resources.ModelResource):
    class Meta:
        model = SorguList

class SorguListAdmin(ImportExportModelAdmin):
    change_list_template = "admin/clear_sorgulist.html"
    list_display = ["id", "sorgu_no", "kontrol"]
    class Meta:
        resource_class = SorguListResource


class LogResource(resources.ModelResource):
    class Meta:
        model = Log

class LogAdmin(ImportExportModelAdmin):

    list_display = ["id", "user", "description", "created_at"]
    search_fields = ["id", "user"]
    list_filter = ["created_at"]
    class Meta:
        resource_class = LogResource

class DepartmanlarAdmin(admin.ModelAdmin):
    model = Departmanlar
    list_display = ["code"]


"""class SayimRaporResource(resources.ModelResource):
    class Meta:
        model = SayimSonrasiRapor"""

"""class SayimRaporAdmin(ImportExportModelAdmin):
    resource_class = SayimRaporResource
    list_display = ["id", "saha_no", "saha_kod", "seri", "sayim", "aciklama"]"""

class SayimSonrasiEnvanterResource(resources.ModelResource):
    class Meta:
        model = SayimSonrasiEnvanter

class SayimSonrasiEnvanterAdmin(ImportExportModelAdmin):
    resource_class = SayimSonrasiEnvanterResource
    list_display = ["id", "saha_no", "saha_kodu", "sayim", "aciklama"]

admin.site.register(SorguList, SorguListAdmin)

admin.site.register(SayimRapor, RaporGirdilerAdmin)

admin.site.register(RaporReferanslari, RaporReferanslariAdmin)

admin.site.register(SayimOncesiEnvanter, HamVeriAdmin)

admin.site.register(Log, LogAdmin)
admin.site.register(Rapor, RaporAdmin)
admin.site.register(Departmanlar, DepartmanlarAdmin)
#admin.site.register(SayimSonrasiRapor, SayimRaporAdmin)
admin.site.register(SayimSonrasiEnvanter, SayimSonrasiEnvanterAdmin)
admin.site.register(UserProfile)
admin.site.register(RaporEnvanter)