# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 17:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('period', models.IntegerField()),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[(b'u', b'Under Review'), (b'a', b'Approved'), (b'r', b'Rejected')], default=b'u', max_length=1)),
                ('applied_date', models.DateTimeField()),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RepaymentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loan.Loan')),
            ],
        ),
    ]
