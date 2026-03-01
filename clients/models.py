from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.


class Client(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='recruitment')
    is_active = models.BooleanField(default=True)
    description = CKEditor5Field(config_name='extends')
    # ordering = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Global Client'
        verbose_name_plural = 'Global Clients'
