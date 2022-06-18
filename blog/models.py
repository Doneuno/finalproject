from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    title_short = models.CharField(max_length=200)
    cover = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    body = RichTextUploadingField(blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    
    