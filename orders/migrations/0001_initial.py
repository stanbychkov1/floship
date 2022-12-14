# Generated by Django 4.1 on 2022-08-19 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=25, unique=True)),
                ('status', models.CharField(choices=[('CREATED', 'Created'), ('STORED', 'Stored'), ('IN PROCESS', 'In process'), ('SENT', 'Sent'), ('DELETED', 'Deleted')], default=None, max_length=25)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('warehouse', models.CharField(choices=[('WAREHOUSE_1', 'Warehouse_1'), ('WAREHOUSE_2', 'Warehouse_2'), ('WAREHOUSE_3', 'Warehouse_3')], max_length=25)),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]
