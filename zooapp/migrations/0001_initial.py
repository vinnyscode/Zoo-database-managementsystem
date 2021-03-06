# Generated by Django 3.1.3 on 2020-12-12 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('speciesname', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('population_status', models.IntegerField()),
            ],
            options={
                'db_table': 'Species',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.IntegerField(primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=30)),
                ('contact_number', models.IntegerField()),
                ('designation', models.CharField(max_length=30)),
                ('salary', models.DecimalField(decimal_places=3, max_digits=10)),
                ('joining_date', models.DateField()),
            ],
            options={
                'db_table': 'Staff',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.IntegerField(primary_key=True, serialize=False)),
                ('cost', models.IntegerField()),
                ('checkin_time', models.TimeField()),
                ('checkout_time', models.TimeField()),
                ('payment_type', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'Ticket',
            },
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('visitor_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('age_group', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField(max_length=12, unique=True)),
                ('address', models.CharField(max_length=30)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitor_staff_id', to='zooapp.staff')),
                ('ticket_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitor_ticket_id', to='zooapp.ticket')),
            ],
            options={
                'db_table': 'Visitor',
            },
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('animal_id', models.IntegerField(primary_key=True, serialize=False)),
                ('animal_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=6)),
                ('birth_date', models.DateField()),
                ('origin', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=30)),
                ('cageno', models.IntegerField(unique=True)),
                ('speciesname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animal_speciesname', to='zooapp.species')),
            ],
            options={
                'db_table': 'Animal',
                'unique_together': {('animal_id', 'cageno')},
            },
        ),
        migrations.CreateModel(
            name='Looks_After',
            fields=[
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='looks_after_animal_id', serialize=False, to='zooapp.animal')),
                ('food', models.CharField(max_length=30)),
                ('feed_time', models.TimeField()),
                ('medicines', models.CharField(max_length=30)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='looks_after_staff_id', to='zooapp.staff')),
            ],
            options={
                'db_table': 'Looks_After',
                'unique_together': {('animal_id', 'staff_id')},
            },
        ),
    ]
