# Generated by Django 4.1.13 on 2024-08-29 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('full_name', models.CharField(max_length=20, verbose_name='نام کامل')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='نام کاربری')),
                ('phone_number', models.CharField(max_length=100, unique=True, verbose_name='شماره همراه')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='ایمیل')),
                ('email_active_code', models.CharField(max_length=48, verbose_name='کد فعال کننده')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='فعال / غیر فعال')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
            },
        ),
    ]
