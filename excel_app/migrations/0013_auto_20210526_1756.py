# Generated by Django 3.1.4 on 2021-05-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_app', '0012_auto_20210526_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hamveri',
            name='ana_yer_tipi',
            field=models.CharField(default='', max_length=5000, verbose_name='Ana Yer Tipi'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='department_code',
            field=models.CharField(default='', max_length=5000, verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='ekipman_no',
            field=models.CharField(default='', max_length=5000, verbose_name='Ekipman No'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='ekipman_parca_kodu',
            field=models.CharField(default='', max_length=5000, verbose_name='Ekipman Parça Kodu'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='organization_code',
            field=models.CharField(default='', max_length=5000, verbose_name='Organization Code'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='parca_tanimi',
            field=models.CharField(default='', max_length=5000, verbose_name='Parça Tanımı'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='quantity',
            field=models.IntegerField(default='', verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='saha_kodu',
            field=models.CharField(default='', max_length=50, verbose_name='Saha Kod'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='saha_no',
            field=models.CharField(default='', max_length=50, verbose_name='Saha No'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='saha_tipi',
            field=models.CharField(default='', max_length=5000, verbose_name='Saha Tipi'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='sahaya_kurulum_tarihi',
            field=models.CharField(default='', max_length=5000, verbose_name='Sahaya Kurulum Tarihi'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='sirket',
            field=models.CharField(default='', max_length=5000, verbose_name='Şirket'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='stok_tipi_1',
            field=models.CharField(default='', max_length=5000, verbose_name='Stok Tipi-1'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='stok_tipi_2',
            field=models.CharField(default='', max_length=5000, verbose_name='Stok Tipi-2'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='stok_tipi_3',
            field=models.CharField(default='', max_length=5000, verbose_name='Stok Tipi-3'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='stok_tipi_4',
            field=models.CharField(default='', max_length=5000, verbose_name='Stok Tipi-4'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='stok_tipi_5',
            field=models.CharField(default='', max_length=5000, verbose_name='Stok Tipi-5'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='stok_tipi_6',
            field=models.CharField(default='', max_length=5000, verbose_name='Stok Tipi-6'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='stok_tipi_7',
            field=models.CharField(default='', max_length=5000, verbose_name='Stok Tipi-7'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='stok_tipi_8',
            field=models.CharField(default='', max_length=5000, verbose_name='Stok Tipi-8'),
        ),
        migrations.AlterField(
            model_name='hamveri',
            name='teslim_alma_tarihi',
            field=models.CharField(default='', max_length=5000, verbose_name='Teslim Alma Tarihi'),
        ),
        migrations.AlterField(
            model_name='log',
            name='description',
            field=models.TextField(default='', max_length=9999999, verbose_name='Yaptığı İşlem'),
        ),
        migrations.AlterField(
            model_name='log',
            name='saha_kod',
            field=models.CharField(default='', max_length=50, verbose_name='Saha Kod'),
        ),
        migrations.AlterField(
            model_name='log',
            name='saha_no',
            field=models.CharField(default='', max_length=50, verbose_name='Saha No'),
        ),
        migrations.AlterField(
            model_name='raporgirdiler',
            name='kategori',
            field=models.CharField(default='', max_length=50, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='raporgirdiler',
            name='kontrol',
            field=models.CharField(default='', max_length=5000, verbose_name='Kontrol'),
        ),
        migrations.AlterField(
            model_name='raporgirdiler',
            name='ref_grup',
            field=models.CharField(default='', max_length=5000, verbose_name='Ref Grup'),
        ),
        migrations.AlterField(
            model_name='raporgirdiler',
            name='saha_kod',
            field=models.CharField(default='', max_length=50, verbose_name='Saha Kod'),
        ),
        migrations.AlterField(
            model_name='raporgirdiler',
            name='saha_no',
            field=models.CharField(default='', max_length=50, verbose_name='Saha No'),
        ),
        migrations.AlterField(
            model_name='raporgirdiler',
            name='sonuc',
            field=models.CharField(default='', max_length=50, verbose_name='Sonuç'),
        ),
        migrations.AlterField(
            model_name='raporgirdiler',
            name='sorgu_no',
            field=models.CharField(default='', max_length=50, verbose_name='Sorgu No'),
        ),
        migrations.AlterField(
            model_name='raporreferanslari',
            name='analiz_no',
            field=models.CharField(default='', max_length=5000, verbose_name='Analiz No'),
        ),
        migrations.AlterField(
            model_name='raporreferanslari',
            name='ekipman_parca_kodu',
            field=models.CharField(default='', max_length=5000, verbose_name='Ekipman Parça Kodu'),
        ),
        migrations.AlterField(
            model_name='raporreferanslari',
            name='grup_tanimi',
            field=models.CharField(default='', max_length=5000, verbose_name='Grup Tanımı'),
        ),
        migrations.AlterField(
            model_name='raporreferanslari',
            name='kategori',
            field=models.CharField(default='', max_length=5000, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='raporreferanslari',
            name='parca_tanimi',
            field=models.CharField(default='', max_length=5000, verbose_name='Parça Tanımı'),
        ),
        migrations.AlterField(
            model_name='raporreferanslari',
            name='rapor_tanimi',
            field=models.CharField(default='', max_length=5000, verbose_name='Rapor Tanımı'),
        ),
        migrations.AlterField(
            model_name='raporreferanslari',
            name='ref',
            field=models.CharField(default='', max_length=5000, verbose_name='Ref'),
        ),
        migrations.AlterField(
            model_name='raporreferanslari',
            name='ref_grup',
            field=models.CharField(default='', max_length=5000, verbose_name='Ref Grup'),
        ),
        migrations.AlterField(
            model_name='raporreferanslari',
            name='sorgu_no',
            field=models.CharField(default='', max_length=5000, verbose_name='Sorgu No'),
        ),
        migrations.AlterField(
            model_name='sorgulist',
            name='check',
            field=models.CharField(default='', max_length=5000, verbose_name='Check'),
        ),
        migrations.AlterField(
            model_name='sorgulist',
            name='kategori',
            field=models.CharField(default='', max_length=5000, verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='sorgulist',
            name='kontrol',
            field=models.CharField(default='', max_length=5000, verbose_name='Kontrol'),
        ),
        migrations.AlterField(
            model_name='sorgulist',
            name='ref_grup',
            field=models.CharField(default='', max_length=5000, verbose_name='Ref Grup'),
        ),
        migrations.AlterField(
            model_name='sorgulist',
            name='sorgu_no',
            field=models.CharField(default='', max_length=5000, verbose_name='Sorgu No'),
        ),
    ]