# Generated by Django 4.1.7 on 2023-03-31 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_category_nike_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nike',
            name='title',
            field=models.CharField(max_length=255, verbose_name='название товара'),
        ),
    ]
