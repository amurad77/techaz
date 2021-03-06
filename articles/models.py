from django.db import models
from django.db.models.fields.files import ImageField
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.conf import settings
from main.models import Tag

from tech.commons import slugify

from tinymce import models as tinymce_models
  

User = get_user_model()

# Create your models here.

class Articles(models.Model):
    #realtion
    owner =  models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    tag = models.ManyToManyField(Tag, related_name='articles')

    #information
    title = models.CharField("Basliq", max_length=256,)
    short_desc = models.CharField("Qisa mezmun", max_length=256)

    content = tinymce_models.HTMLField('Mezmunn')

    image = models.ImageField("Şəkil", upload_to='article_images', null=True, blank=True)
    cover_image = models.ImageField("Qapak örtüyü", upload_to='aritcle_cover_images', null=True, blank=True)
    views = models.PositiveIntegerField(default=3, blank=True, null=True)
    slug = models.SlugField('Slug', max_length=110, unique=True)
    file_abs_url = models.URLField(_("abs url"), default='', max_length=200)
    type = models.CharField("Type", max_length=30, editable=False, default='articles')

    # moderations
    is_published = models.BooleanField('is published', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Megale'
        verbose_name_plural = 'Megaleler'
        ordering = ('-created_at',)

    def add_view_count(self):
        self.views +=3
        self.save()
        return True


