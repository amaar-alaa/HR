# Generated by Django 3.1.3 on 2021-05-07 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Depart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=88)),
                ('cost', models.IntegerField()),
                ('selling', models.IntegerField()),
                ('desc', models.TextField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('curency', models.CharField(max_length=50)),
                ('depatr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.depart')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.unit')),
            ],
        ),
    ]
