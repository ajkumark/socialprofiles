# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fullcontactapp', '0004_auto_20150303_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='AprilFool',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=90)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
