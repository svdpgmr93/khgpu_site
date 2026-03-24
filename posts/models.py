from django.db import models

# Create your models here.
class BasePost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    icon = models.ImageField()