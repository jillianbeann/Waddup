# Generated by Django 4.1.7 on 2023-03-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('event_date_time', models.DateTimeField()),
                ('event_type', models.CharField(choices=[('Party', 'Party'), ('Concert', 'Concert'), ('Comedy Show', 'Comedy Show'), ('Other', 'Other')], default='Party', max_length=15)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('desc', models.TextField()),
                ('event_price', models.IntegerField(default=0)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('age', models.IntegerField(choices=[(0, '18+'), (1, '21+'), (2, 'All ages welcome')], default=0)),
            ],
            options={
                'ordering': ('event_date_time',),
            },
        ),
    ]
