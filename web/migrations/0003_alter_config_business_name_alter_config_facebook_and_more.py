# Generated by Django 4.1.5 on 2023-03-12 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_new_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='business_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='business name'),
        ),
        migrations.AlterField(
            model_name='config',
            name='facebook',
            field=models.URLField(blank=True, max_length=240, null=True, verbose_name='facebook'),
        ),
        migrations.AlterField(
            model_name='config',
            name='flirk',
            field=models.URLField(blank=True, max_length=240, null=True, verbose_name='flirk'),
        ),
        migrations.AlterField(
            model_name='config',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='config/', verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='config',
            name='pinterest',
            field=models.URLField(blank=True, max_length=240, null=True, verbose_name='pinterest'),
        ),
        migrations.AlterField(
            model_name='config',
            name='telegram',
            field=models.URLField(blank=True, max_length=240, null=True, verbose_name='telegram'),
        ),
        migrations.AlterField(
            model_name='config',
            name='twitter',
            field=models.URLField(blank=True, max_length=240, null=True, verbose_name='twitter'),
        ),
    ]
