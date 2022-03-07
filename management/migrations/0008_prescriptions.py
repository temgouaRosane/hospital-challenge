# Generated by Django 3.2.9 on 2022-02-02 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_appointments_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptoms', models.TextField(max_length=999999)),
                ('prescription', models.TextField(max_length=999999)),
                ('prescripted_date', models.DateTimeField(auto_now_add=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.appointments')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.doctors')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.patients')),
            ],
        ),
    ]
