# Generated by Django 4.2.7 on 2025-01-22 15:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('party', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='candidates/')),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ElectionOfficer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='officers/')),
                ('fullname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField()),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='EligibleVoter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=15, unique=True)),
                ('is_eligible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='voters/')),
                ('fullname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.candidate')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='vote.election')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vote.voter')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='vote.election'),
        ),
    ]
