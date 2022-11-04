# Generated by Django 4.1.3 on 2022-11-03 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_ordermodel_qr_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitemsmodel',
            name='has_attended',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderitemsmodel',
            name='ticket',
            field=models.ImageField(default='', upload_to='tickets'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TicketModel',
        ),
    ]
