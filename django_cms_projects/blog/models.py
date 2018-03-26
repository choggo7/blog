from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



#category
class category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

def __init__(self):
    return self.name
          
#post
class post(models.Model):
    STATUS_CHOICES = (
    ('draft','Draft'),
    ('published','Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique=True)
    content = models.TextField()
    seo_title = models.CharField(max_length=250)
    seo_description = models.CharField(max_length=250)
    author = models.ForeignKey(User,related_name='blog_posts',default=1,on_delete=models.CASCADE,)
    category = models.ForeignKey(category,)
    published = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=365))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9,choices=STATUS_CHOICES,default='draft')
    pic = models.ImageField(upload_to="upload_images",blank='True',default='default.jpg')

def __init__(self):
    return self.title
