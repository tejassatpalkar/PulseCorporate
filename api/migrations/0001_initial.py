# Generated by Django 3.1.4 on 2020-12-27 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('past_sponsorship', models.IntegerField(default=0)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_changed', models.DateTimeField(auto_now=True)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('linkedin', models.URLField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='api.company')),
            ],
        ),
    ]