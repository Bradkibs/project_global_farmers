# Generated by Django 4.1.7 on 2023-03-31 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspector_api', '0002_inspector_is_registered_alter_inspector_secret_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspector',
            name='secret_key',
            field=models.CharField(default='.321ytrewq', help_text='enter your 8 digit/character key given', max_length=100),
        ),
    ]
