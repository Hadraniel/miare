# Generated by Django 4.1.3 on 2022-11-18 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courier', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeeklyIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_start', models.DateField(verbose_name='week start')),
                ('total_income', models.IntegerField(default=0, verbose_name='total income')),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courier.courier')),
            ],
            options={
                'verbose_name': 'weekly income',
                'verbose_name_plural': 'weekly incomes',
                'unique_together': {('courier', 'week_start')},
            },
        ),
        migrations.CreateModel(
            name='DailyIncome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='date')),
                ('total_income', models.IntegerField(default=0)),
                ('courier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courier.courier')),
            ],
            options={
                'verbose_name': 'daily income',
                'verbose_name_plural': 'daily incomes',
                'unique_together': {('courier', 'date')},
            },
        ),
    ]
