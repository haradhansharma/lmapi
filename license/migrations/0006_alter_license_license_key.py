# Generated by Django 5.0.4 on 2024-04-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0005_alter_license_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='license_key',
            field=models.CharField(editable=False, help_text='License data. Required when updating a license.', max_length=100, unique=True),
        ),
    ]