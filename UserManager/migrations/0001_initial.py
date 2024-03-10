# Generated by Django 3.2.13 on 2022-06-21 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clg_id', models.CharField(max_length=4, unique=True, verbose_name='Collage Id')),
                ('clg_name', models.CharField(max_length=100, verbose_name='Collage Name')),
            ],
        ),
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream_id', models.CharField(max_length=5, unique=True, verbose_name='Stream Id')),
                ('stream_name', models.CharField(max_length=100, verbose_name='Stream Name')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('reg_no', models.AutoField(primary_key=True, serialize=False, unique=True, verbose_name='Registration Number')),
                ('fname', models.CharField(max_length=50, verbose_name='First Name')),
                ('lname', models.CharField(max_length=50, verbose_name='Last Name')),
                ('contect_no', models.IntegerField(verbose_name='Contect No')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email ID')),
                ('is_participant', models.BooleanField(default=False, verbose_name='Participant')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Event Committee')),
                ('clg', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserManager.college', verbose_name='Collage')),
                ('stream', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='UserManager.stream', verbose_name='Stream')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event_Committee',
            fields=[
                ('reg_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='UserManager.user')),
                ('committee_id', models.CharField(max_length=20, unique=True)),
                ('yearOfStudy', models.IntegerField()),
                ('is_coordinator', models.BooleanField(default=False)),
                ('is_event_head', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('in_sponsorship', models.BooleanField(default=False)),
                ('in_publicity', models.BooleanField(default=False)),
                ('in_criative', models.BooleanField(default=False)),
                ('in_technical', models.BooleanField(default=False)),
                ('in_volunteering', models.BooleanField(default=False)),
                ('in_logistics', models.BooleanField(default=False)),
                ('in_graphics', models.BooleanField(default=False)),
                ('in_eventManagement', models.BooleanField(default=False)),
            ],
        ),
    ]