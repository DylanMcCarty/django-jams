# Generated by Django 4.1.3 on 2022-11-17 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0005_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('length', models.FloatField(null=True)),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jams.album')),
                ('artist_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='jams.artist')),
            ],
        ),
    ]
