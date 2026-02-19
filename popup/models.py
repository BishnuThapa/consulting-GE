from django.db import models

# Create your models here.
class Popup(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='activities')
    is_active = models.BooleanField(default=True)
    ordering = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Popup Notice'
        verbose_name_plural = 'Popup Notice'