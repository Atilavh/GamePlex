from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(verbose_name='عنوان در دسته بندی', db_index=True, unique=True, max_length=30)
    url_title = models.CharField(verbose_name='عنوان در url', db_index=True, max_length=40)
    is_active = models.BooleanField(default=False, verbose_name='فعال شده / نشده')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


# Create your models here.
class Tournament(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان تورنومنت')
    mode = models.CharField(max_length=15, verbose_name='حالت بازی')
    prize = models.IntegerField(verbose_name='مقدار جایزه')
    date = models.DateTimeField(verbose_name='تاریخ تورنومنت')
    ticketamount = models.IntegerField(verbose_name='هزینه ورودی')
    image = models.ImageField(upload_to='images', verbose_name='عکس تورنومنت')
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=200, unique=True,
                            verbose_name='عنوان در url', editable=True)
    category = models.ManyToManyField(Category, related_name='tournament_categories', verbose_name='دسته بندی ها')
    is_active = models.BooleanField(verbose_name='فعال شده / نشده')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('tournament_detail', args=[self.slug])

    class Meta:
        verbose_name = 'تورنومنت'
        verbose_name_plural = 'تورنومنت ها'

    def __str__(self):
        return self.title
