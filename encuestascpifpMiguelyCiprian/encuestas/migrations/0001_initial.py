# Generated by Django 3.1.1 on 2020-12-02 09:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=45)),
            ],
            options={
                'ordering': ['tipo'],
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=100)),
                ('tipo_pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.tipo_pregunta')),
            ],
            options={
                'ordering': ['pregunta'],
            },
        ),
        migrations.CreateModel(
            name='Opcion_Pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.CharField(max_length=100)),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.pregunta')),
            ],
            options={
                'ordering': ['opcion'],
            },
        ),
    ]