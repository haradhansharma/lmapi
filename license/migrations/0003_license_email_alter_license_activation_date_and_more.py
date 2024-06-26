# Generated by Django 5.0.4 on 2024-04-09 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('license', '0002_alter_license_activation_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='email',
            field=models.EmailField(default='', max_length=254),
            # preserve_default=False,
        ),
        migrations.AlterField(
            model_name='license',
            name='activation_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='license',
            name='license_key',
            field=models.CharField(editable=False, help_text='Encrypted configuration data. Required when updating a license.', max_length=100, unique=True),
        ),
    ]
