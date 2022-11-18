# Generated by Django 4.1.3 on 2022-11-18 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.PositiveIntegerField(verbose_name='payment')),
                ('created_at', models.DateField(verbose_name='date')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courier.courier')),
            ],
            options={
                'verbose_name': 'trip',
                'verbose_name_plural': 'trips',
            },
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.PositiveIntegerField(verbose_name='payment')),
                ('created_at', models.DateField(verbose_name='date')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courier.courier')),
            ],
            options={
                'verbose_name': 'penalty',
                'verbose_name_plural': 'penalties',
            },
        ),
        migrations.CreateModel(
            name='Bonus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.PositiveIntegerField(verbose_name='payment')),
                ('created_at', models.DateField(verbose_name='date')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courier.courier')),
            ],
            options={
                'verbose_name': 'bonus',
                'verbose_name_plural': 'bonuses',
            },
        ),
    ]