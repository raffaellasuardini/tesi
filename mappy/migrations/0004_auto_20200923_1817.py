# Generated by Django 3.1 on 2020-09-23 16:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mappy', '0003_auto_20200923_1806'),
    ]

    operations = [
        migrations.AddField(
            model_name='coord',
            name='id',
            field=models.AutoField(auto_created=True, default=12, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coord',
            name='object_label',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
