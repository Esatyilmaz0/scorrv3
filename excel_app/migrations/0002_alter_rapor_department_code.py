# Generated by Django 3.2.3 on 2021-06-01 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excel_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapor',
            name='department_code',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='excel_app.departmanlar'),
        ),
    ]