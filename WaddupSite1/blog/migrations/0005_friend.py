# Generated by Django 4.1.7 on 2023-02-19 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_event_event_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Requested', 'Requested'), ('Concert', 'Accepted'), ('Denied', 'Denied')], default='Requested', max_length=20)),
            ],
        ),
    ]