# Generated by Django 4.1.3 on 2022-11-04 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_remove_ordermodel_qr_img_orderitemsmodel_qr_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitemsmodel',
            name='qr_img',
            field=models.ImageField(blank=True, height_field=290, null=True, upload_to='QR', width_field=290),
        ),
    ]
