# Generated by Django 2.2.1 on 2019-12-29 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=32)),
                ('type_pic', models.ImageField(upload_to='store_static/img')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('store', models.CharField(max_length=128)),
                ('price', models.FloatField()),
                ('safe_date', models.DateField()),
                ('picture', models.ImageField(upload_to='store_static/img')),
                ('number', models.IntegerField()),
                ('description', models.TextField()),
                ('status', models.IntegerField(default=1)),
                ('goods_type', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.GoodsType')),
            ],
        ),
    ]
