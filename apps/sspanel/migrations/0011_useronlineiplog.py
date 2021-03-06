# Generated by Django 2.2.1 on 2019-05-27 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("sspanel", "0010_auto_20190522_1326")]

    operations = [
        migrations.CreateModel(
            name="UserOnLineIpLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(db_index=True)),
                ("node_id", models.IntegerField()),
                ("ip", models.CharField(max_length=128)),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                "verbose_name_plural": "用户在线IP",
                "ordering": ["-created_at"],
                "unique_together": {("node_id", "created_at")},
            },
        )
    ]
