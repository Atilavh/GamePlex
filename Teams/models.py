from django.db import models
from Tournaments.models import Tournament
from accounts_module.models import User


# Create your models here.

class Team(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان تیم')
    image = models.ImageField(upload_to='Teams/', verbose_name="عکس تیم")
    earnedamount = models.IntegerField(verbose_name='مقدار برنده شده')
    captain = models.CharField(max_length=30, verbose_name='کاپیتان تیم')
    tournament = models.ForeignKey(
        Tournament,
        on_delete=models.CASCADE,
        verbose_name='تورنومنت های برنده شده',
        null=True,
        blank=True
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='یوزر های ثبت شده',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'تیم'
        verbose_name_plural = 'تیم ها'

    def __str__(self):
        return self.title
