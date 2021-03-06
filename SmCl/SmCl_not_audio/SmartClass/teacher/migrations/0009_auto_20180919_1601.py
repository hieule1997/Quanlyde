# Generated by Django 2.1 on 2018-09-19 09:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0008_auto_20180917_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diemso',
            name='bai_lam_id',
        ),
        migrations.AddField(
            model_name='diemso',
            name='bai_lam',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='diemso',
            name='de_id',
            field=models.ForeignKey(db_column='de_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='teacher.De'),
        ),
        migrations.AlterField(
            model_name='diemso',
            name='diem',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='diemso',
            name='loai_diem',
            field=models.CharField(max_length=255),
        ),
    ]
