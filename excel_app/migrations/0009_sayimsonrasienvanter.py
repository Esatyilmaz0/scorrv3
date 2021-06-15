# Generated by Django 3.2.3 on 2021-06-02 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excel_app', '0008_alter_sayimoncesienvanter_rapor'),
    ]

    operations = [
        migrations.CreateModel(
            name='SayimSonrasiEnvanter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saha_no', models.CharField(default='', max_length=50, verbose_name='Saha No')),
                ('saha_kodu', models.CharField(default='', max_length=50, verbose_name='Saha Kod')),
                ('ekipman_no', models.CharField(default='', max_length=5000, verbose_name='Ekipman No')),
                ('ekipman_seri_no', models.CharField(default='', max_length=5000, verbose_name='Ekipman Seri No')),
                ('ekipman_parca_kodu', models.CharField(default='', max_length=5000, verbose_name='Ekipman Parça Kodu')),
                ('parca_tanimi', models.CharField(default='', max_length=5000, verbose_name='Parça Tanımı')),
                ('department_code', models.CharField(default='', max_length=5000, verbose_name='Department')),
                ('quantity', models.IntegerField(default='', verbose_name='Quantity')),
                ('aciklama', models.CharField(default='', max_length=5000, verbose_name='Açıklama')),
                ('sayim', models.IntegerField(default=0, verbose_name='Sayim')),
                ('rapor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='excel_app.rapor')),
            ],
        ),
    ]