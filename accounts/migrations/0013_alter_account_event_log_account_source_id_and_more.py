# Generated by Django 4.1.1 on 2022-10-07 02:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0012_account_event_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account_event_log',
            name='account_source_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='account_event_log',
            name='user_source_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]