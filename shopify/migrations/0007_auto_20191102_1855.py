# Generated by Django 2.2.6 on 2019-11-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0006_auto_20191102_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variant',
            name='option2',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='variant',
            name='option3',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
