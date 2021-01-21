from django.db import models
from .validators import file_size
from .validators import validate_file_extension
from django.core.validators import validate_slug
from captcha.fields import CaptchaField

# Create your models here.
class Video(models.Model):
    caption=models.CharField(max_length=20, validators=[validate_slug])
    video=models.FileField(upload_to="video/%y",validators=[file_size, validate_file_extension])
    def __str__(self):
        return self.caption
