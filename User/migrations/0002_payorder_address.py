# Generated by Django 2.2.1 on 2019-12-30 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payorder',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='User.Address'),
            preserve_default=False,
        ),
    ]
