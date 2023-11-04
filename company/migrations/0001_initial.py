# Generated by Django 4.2.6 on 2023-10-20 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('addr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comp_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identify', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.EmailField(blank=True, max_length=255)),
                ('contact', models.CharField(max_length=150)),
                ('activity', models.CharField(max_length=250)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addr.addr_info')),
            ],
        ),
    ]