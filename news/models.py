from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from extensions import utils 

# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length = 250,verbose_name = 'عنوان دسته بندی')
    slug = models.SlugField(max_length = 500,verbose_name='ادرس دسته بندی')
    description=models.TextField(verbose_name='توضیحات ',null=True,blank = True)
    status=models.BooleanField(default=True,verbose_name='ایا نشان داده شود؟')
    position=models.IntegerField(verbose_name='موقعیت نمایش')
    thumbnail = models.ImageField(upload_to= 'images',null= True, blank=True)
    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        ordering=('-position',)
    def __str__(self):
        return self.title

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','پیش نویس'),
        ('published','منتشر شده')
    )
    thumbnail = models.ImageField(upload_to= 'images',null= True, blank=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,verbose_name='دسته بندی',null=True)
    title = models.CharField(max_length = 250,verbose_name = 'عنوان خبر')
    slug = models.SlugField(max_length = 500, unique_for_date = 'publish')
    body = models.TextField(verbose_name='متن خبر',null=True,blank = True)
    publish = models.DateTimeField(default = timezone.now,verbose_name='تاریخ انتشار')
    created=models.DateTimeField(auto_now_add =timezone.now )
    updated=models.DateTimeField(auto_now=timezone.now)
    status=models.CharField(max_length=15,default = 'draft',choices=STATUS_CHOICES,verbose_name='وضعیت')
    author=models.ForeignKey(User,on_delete=models.SET_DEFAULT,default = 1,verbose_name='نویسنده')
    price = models.DecimalField(max_digits=5, decimal_places=2, null = True, blank = True)
    def jalali_publish(self):
        return utils.jalali_converter(self.publish)
    jalali_publish.short_description='تاریخ انتشار '
    def jalali_created(self):
        return utils.jalali_converter(self.created)
    jalali_created.short_description='تاریخ ایجاد '
    def jalali_updated(self):
        return utils.jalali_converter(self.updated)
    jalali_updated.short_description='تاریخ به روزرسانی '
    
    def __str__(self):
        return self.title
    class Meta:
        ordering=('-publish',)
        verbose_name = 'خبر'
        verbose_name_plural = 'خبرها'







    