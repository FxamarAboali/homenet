# Generated by Django 2.2.3 on 2019-07-29 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_auto_20190726_1938'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='fee',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]