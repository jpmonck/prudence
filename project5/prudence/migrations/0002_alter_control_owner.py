# Generated by Django 4.2.13 on 2024-08-05 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("prudence", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="control",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="controls",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
