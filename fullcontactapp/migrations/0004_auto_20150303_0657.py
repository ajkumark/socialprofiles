# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fullcontactapp', '0003_notfoundcontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notfoundcontact',
            name='count',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
