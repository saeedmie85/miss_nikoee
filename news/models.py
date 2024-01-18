from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 

# Create your models here.
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','پیش نویس'),
        ('published','منتشر شده')
    )
    
    title = models.CharField(max_length = 250,verbose_name = 'عنوان خبر')
    slug = models.SlugField(max_length = 500, unique_for_date = 'publish')
    body = models.TextField(verbose_name='متن خبر',null=True,blank = True)
    publish = models.DateTimeField(default = timezone.now,verbose_name='تاریخ انتشار')
    created=models.DateTimeField(auto_now_add =timezone.now )
    updated=models.DateTimeField(auto_now=timezone.now)
    status=models.CharField(max_length=15,default = 'draft',choices=STATUS_CHOICES)
    author=models.ForeignKey(User,on_delete=models.SET_DEFAULT,default = 1)
    def __str__(self):
        return self.title
    class Meta:
        ordering=('-publish',)
        verbose_name = 'خبر'
        verbose_name_plural = 'خبرها'







    