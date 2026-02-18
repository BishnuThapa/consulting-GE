from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# from ckeditor.fields import RichTextField
# Create your models here.


class ChairmanMessage(models.Model):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    featured_image = models.ImageField(
        upload_to='principal', blank=True, null=True, default='')
    description = CKEditor5Field(config_name='extends')

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Message From Chairman'
        verbose_name_plural = 'Message From Chairman'


class About(models.Model):
    heading = models.CharField(max_length=255)
    sub_heading = models.CharField(max_length=255)
    featured_image = models.ImageField(
        upload_to='about', blank=True, null=True, default='')
    description = CKEditor5Field(config_name='extends')

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'


class WhyUs(models.Model):
    heading = models.CharField(max_length=255)
    image_icon = models.ImageField(
        upload_to='about', blank=True, null=True, default='')
    featured_image = models.ImageField(
        upload_to='about', blank=True, null=True, default='')
    experience=models.IntegerField(default=0)
    short_description = models.TextField()
    description = CKEditor5Field(config_name='extends')

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = 'Why us'
        verbose_name_plural = 'Why us'

