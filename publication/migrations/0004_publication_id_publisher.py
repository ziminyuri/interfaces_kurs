# Generated by Django 2.2.2 on 2019-06-14 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0003_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='ID_publisher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='publication.Publisher'),
            preserve_default=False,
        ),
    ]
