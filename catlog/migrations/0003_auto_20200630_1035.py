# Generated by Django 3.0.7 on 2020-06-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0002_auto_20200630_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]