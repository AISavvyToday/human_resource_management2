# Generated by Django 2.2 on 2020-01-24 14:20

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('small_small_hr', '0010_auto_20200121_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['user__first_name', 'user__last_name', 'user__username', 'created'], 'verbose_name': 'Staff Profile', 'verbose_name_plural': 'Staff Profiles'},
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, default='', verbose_name='Addresss'),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Birthday'),
        ),
        migrations.AddField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True, verbose_name='Data'),
        ),
        migrations.AddField(
            model_name='profile',
            name='end_date',
            field=models.DateField(blank=True, default=None, help_text='The end date of employment', null=True, verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='profile',
            name='leave_days',
            field=models.PositiveIntegerField(blank=True, default=21, help_text='Number of leave days allowed in a year.', verbose_name='Leave days'),
        ),
        migrations.AddField(
            model_name='profile',
            name='modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Modified'),
        ),
        migrations.AddField(
            model_name='profile',
            name='overtime_allowed',
            field=models.BooleanField(blank=True, default=False, verbose_name='Overtime allowed'),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='', max_length=128, region=None, verbose_name='Phone'),
        ),
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='small_small_hr.Role', verbose_name='Role'),
        ),
        migrations.AddField(
            model_name='profile',
            name='sex',
            field=models.CharField(blank=True, choices=[('0', 'Not Known'), ('1', 'Male'), ('2', 'Female'), ('9', 'Not Applicable')], db_index=True, default='0', max_length=1, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='profile',
            name='sick_days',
            field=models.PositiveIntegerField(blank=True, default=10, help_text='Number of sick days allowed in a year.', verbose_name='Sick days'),
        ),
        migrations.AddField(
            model_name='profile',
            name='start_date',
            field=models.DateField(blank=True, default=None, help_text='The start date of employment', null=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='annualleave',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='small_small_hr.Profile', verbose_name='Staff Member'),
        ),
        migrations.AlterField(
            model_name='leave',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='small_small_hr.Profile', verbose_name='Staff Member'),
        ),
        migrations.AlterField(
            model_name='overtime',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='small_small_hr.Profile', verbose_name='Staff Member'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', help_text='A square image works best', upload_to='profile_pics', verbose_name='Profile Image'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='staffdocument',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='small_small_hr.Profile', verbose_name='Staff Member'),
        ),
        migrations.DeleteModel(
            name='StaffProfile',
        ),
    ]