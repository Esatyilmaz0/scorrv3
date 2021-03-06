# Generated by Django 3.2.3 on 2021-06-02 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excel_app', '0012_delete_sayimsonrasirapor'),
    ]

    operations = [
        migrations.CreateModel(
            name='SayimRapor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saha_no', models.CharField(default='', max_length=50, verbose_name='Saha No')),
                ('saha_kod', models.CharField(default='', max_length=50, verbose_name='Saha Kod')),
                ('ref_1', models.IntegerField(verbose_name='Referans-1')),
                ('ref_2', models.IntegerField(verbose_name='Referans-2')),
                ('ref_3', models.IntegerField(verbose_name='Referans-3')),
                ('ref_4', models.IntegerField(verbose_name='Referans-4')),
                ('ref_5', models.IntegerField(verbose_name='Referans-5')),
                ('ref_6', models.IntegerField(verbose_name='Referans-6')),
                ('ref_grup', models.CharField(default='', max_length=5000, verbose_name='Ref Grup')),
                ('sonuc', models.CharField(default='', max_length=50, verbose_name='Sonuç')),
                ('kontrol', models.CharField(default='', max_length=5000, verbose_name='Kontrol')),
                ('kategori', models.CharField(default='', max_length=50, verbose_name='Kategori')),
                ('sorgu_no', models.CharField(default='', max_length=50, verbose_name='Sorgu No')),
                ('aciklama', models.CharField(blank=True, default='', max_length=5000, verbose_name='Açıklama')),
                ('is_sayim_sonrasi', models.BooleanField(default=False, verbose_name='Sayım Sonrası Girdisi Mi?')),
                ('rapor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='girdiler', to='excel_app.rapor')),
            ],
        ),
        migrations.RemoveField(
            model_name='sayimsonrasienvanter',
            name='ekipman_no',
        ),
        migrations.DeleteModel(
            name='SayimOncesiRapor',
        ),
    ]
