# Generated by Django 3.0.7 on 2020-06-30 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catlog', '0008_auto_20200630_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='code',
            field=models.TextField(unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='nutrition_grade_fr',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product', name='quantity', field=models.TextField(),
        ),
    ]