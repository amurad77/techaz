from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
# Create your models here.
from django.conf import settings

from django.core.files.storage import FileSystemStorage

class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )
    # information's 
    education = models.CharField("Education", max_length=256, null=True, blank=True)
    gender = models.CharField('Gender', max_length=1, null=True, blank=True, choices=GENDER_CHOICES)
    image = models.ImageField("Image", upload_to='users_images', null=True, blank=True)
    position = models.CharField("Position", max_length=100, null=True, blank=True)
    birthday = models.DateField("Birthday", null=True, blank=True)
    
    # moderation's
    status = models.BooleanField('Status', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'
    


class Config(models.Model):
    apiKey = models.CharField('apiKey', default = "AIzaSyDV-DLZPcnGX_5aHY9icwvOz2JE12pe-eU", max_length=256)
    authDomain = models.CharField('authDomain', default = "techaz-bfae3.firebaseapp.com", max_length=256)
    projectId = models.CharField('projectId', default = "techaz-bfae3", max_length=256)
    storageBucket = models.CharField('storageBucket', default = "techaz-bfae3.appspot.com", max_length=256)
    messagingSenderId = models.CharField('messagingSenderId', default = "186177661017", max_length=256)
    appId = models.CharField('appId', default = "1:186177661017:web:3a90c4487e1af1e3e22948", max_length=256)