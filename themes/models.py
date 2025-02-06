from django.db import models

# Model for theme.
class SiteSettings(models.Model):
    banner = models.ImageField(upload_to='media/site')
    caption = models.TextField()