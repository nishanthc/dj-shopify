# Generated by Django 2.2.6 on 2019-11-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
