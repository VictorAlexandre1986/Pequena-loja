# Generated by Django 3.2.5 on 2021-08-04 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_dono_ownew'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='dono_ownew',
            new_name='donoownew',
        ),
    ]
