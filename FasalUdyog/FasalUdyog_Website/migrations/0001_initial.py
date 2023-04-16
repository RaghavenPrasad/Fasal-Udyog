# Generated by Django 4.1.7 on 2023-04-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="center",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("center_id", models.CharField(max_length=45)),
                ("handler_name", models.CharField(max_length=45)),
                ("village_name", models.CharField(max_length=45)),
                ("handler_id", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="farmer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("farmer_id", models.CharField(max_length=45)),
                ("farmer_name", models.CharField(max_length=45)),
                ("aadhaar_id", models.CharField(max_length=45)),
                ("father_name", models.CharField(max_length=45)),
                ("village_name", models.CharField(max_length=45)),
                ("category", models.CharField(max_length=45)),
                ("gender", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="farmer_deposits_stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("farmer_id", models.CharField(max_length=45)),
                ("item_id", models.CharField(max_length=45)),
                ("item_name", models.CharField(max_length=45)),
                ("quantity", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="handler",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("handler_id", models.CharField(max_length=45)),
                ("handler_name", models.CharField(max_length=45)),
                ("handler_contact", models.CharField(max_length=45)),
                ("handler_address", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="manager",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("manager_id", models.CharField(max_length=45)),
                ("manager_name", models.CharField(max_length=45)),
                ("manager_contact", models.CharField(max_length=45)),
                ("manager_address", models.CharField(max_length=45)),
                ("manager_pass", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="orders",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_id", models.IntegerField()),
                ("item_id", models.CharField(max_length=45)),
                ("item_name", models.CharField(max_length=45)),
                ("quantity", models.CharField(max_length=45)),
                ("store_address", models.CharField(max_length=45)),
                ("zip", models.CharField(max_length=45)),
                ("locality", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="stock_center",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_id", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("msp", models.IntegerField()),
                ("item_name", models.CharField(max_length=45)),
                ("center_id", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="stock_farmer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_id", models.CharField(max_length=45)),
                ("quantity", models.CharField(max_length=45)),
                ("msp", models.CharField(max_length=45)),
                ("item_name", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="stock_total",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_id", models.IntegerField()),
                ("msp", models.IntegerField()),
                ("quantity", models.IntegerField()),
                ("value", models.CharField(max_length=45)),
                ("item_name", models.CharField(max_length=45)),
                ("center_id", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="store",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("store_id", models.CharField(max_length=45)),
                ("district_name", models.CharField(max_length=45)),
                ("handler_id", models.CharField(max_length=45)),
                ("handler_name", models.CharField(max_length=45)),
                ("locality", models.CharField(max_length=45)),
                ("zip", models.CharField(max_length=45)),
                ("store_address", models.CharField(max_length=45)),
                ("manager_id", models.CharField(max_length=45)),
                ("GSTIN", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="store_has_orders",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("order_id", models.IntegerField()),
                ("store_id", models.CharField(max_length=45)),
                ("item_name", models.CharField(max_length=45)),
                ("item_id", models.CharField(max_length=45)),
                ("quantity", models.CharField(max_length=45)),
                ("orders_has_storecol", models.CharField(max_length=45)),
            ],
        ),
    ]
