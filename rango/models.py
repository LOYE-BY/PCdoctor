# coding=utf-8
from django.db import models
# from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    """table_Category"""
    name = models.CharField(max_length=128, unique=True)

    # chongzai  hanshu
    def __unicode__(self):
        return self.name


class Page(models.Model):
    """table_Page"""
    category = models.ForeignKey(Category)  # 外键
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

'''
class UserProfile(models.Model):
    """增加用户属性"""
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
'''
