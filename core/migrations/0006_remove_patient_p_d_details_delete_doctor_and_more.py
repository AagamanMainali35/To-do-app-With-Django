# Generated by Django 5.0.7 on 2024-08-13 02:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_adress_patient_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='p_d_details',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='patient',
        ),
    ]
