# Generated by Django 4.2.6 on 2023-10-20 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hvm', '0010_receiver_contact_number_receiver_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='accompanying',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='leadvisitor',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]