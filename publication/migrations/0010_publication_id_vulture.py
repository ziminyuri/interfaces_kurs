# Generated by Django 2.2.2 on 2019-06-14 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0009_vulture'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='ID_vulture',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.DO_NOTHING, to='publication.Vulture'),
            preserve_default=False,
        ),
    ]