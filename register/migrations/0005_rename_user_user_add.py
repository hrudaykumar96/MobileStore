# Generated by Django 4.1.6 on 2023-04-02 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("register", "0004_rename_users_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="User",
            new_name="User_add",
        ),
    ]
