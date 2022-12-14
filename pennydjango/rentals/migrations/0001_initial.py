# Generated by Django 2.2 on 2019-04-15 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RentProperty',
            fields=[
                ('model_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('price', models.PositiveIntegerField()),
                ('contact', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=7, max_digits=10)),
                ('about', models.TextField(blank=True, max_length=512, null=True)),
                ('bedrooms', models.IntegerField()),
                ('baths', models.IntegerField()),
                ('pets_allowed', models.BooleanField(default=True)),
                ('amenities', models.TextField()),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rent_properties', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
