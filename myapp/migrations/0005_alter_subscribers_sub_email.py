# Generated by Django 3.2.5 on 2022-01-08 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_contact_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribers',
            name='Sub_email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
