# Generated by Django 3.2.3 on 2021-06-12 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_app', '0022_raporenvanter_aciklama'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bakimci',
            field=models.BooleanField(default=False, verbose_name='Bakımcı'),
        ),
    ]
