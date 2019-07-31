# Generated by Django 2.1.10 on 2019-07-31 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('contact_num', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('coming', 'Coming'), ('on going', 'On Going'), ('not coming', 'Not Coming'), ('reliver', 'Reliver'), ('on call', 'On Call'), ('not sure', 'Not Sure'), ('leave', 'Leave'), ('Out', 'Out')], max_length=60, null=True)),
                ('date_join', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specialty', models.CharField(max_length=60)),
                ('sub_specialty', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='physician',
            name='specialization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.Specialization'),
        ),
    ]
