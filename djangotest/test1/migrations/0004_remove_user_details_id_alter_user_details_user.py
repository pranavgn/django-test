# Generated by Django 4.0.5 on 2022-06-05 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test1', '0003_remove_user_details_user_id_user_details_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_details',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
