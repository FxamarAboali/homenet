# Generated by Django 2.2 on 2019-04-23 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rentals', '0005_rentpropertyimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('address', models.CharField(max_length=255)),
                ('center', models.CharField(max_length=64)),
                ('radius', models.PositiveIntegerField()),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('agent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
