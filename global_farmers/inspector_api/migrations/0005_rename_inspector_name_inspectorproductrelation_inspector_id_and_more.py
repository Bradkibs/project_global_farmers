# Generated by Django 4.1.7 on 2023-04-06 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspector_api', '0004_inspectorproductrelation_delete_inspector'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspectorproductrelation',
            old_name='inspector_name',
            new_name='inspector_id',
        ),
        migrations.RenameField(
            model_name='inspectorproductrelation',
            old_name='product_inspected',
            new_name='product_inspected_id',
        ),
    ]