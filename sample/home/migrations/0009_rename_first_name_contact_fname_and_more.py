# Generated by Django 4.1.6 on 2023-02-27 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_fname_contact_first_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='First_Name',
            new_name='fName',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Last_Name',
            new_name='lName',
        ),
    ]
