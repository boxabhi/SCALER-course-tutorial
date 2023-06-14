
from statistics import mode
from turtle import ondrag, up
from django.db import models
import uuid
from django.contrib.auth.models import User

class BaseModel(models.Model):
    uid= models.UUIDField(primary_key=True ,editable=False , default=uuid.uuid4)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)


    class Meta:
        abstract = True


class BlogCategory(BaseModel):
    category_name = models.CharField(max_length=100)


class Blog(BaseModel):
    category = models.ForeignKey(BlogCategory , on_delete=models.CASCADE , null=True , blank = True)
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name="blogs")
    title = models.CharField(max_length=500)
    blog_text = models.TextField()
    main_image = models.ImageField(upload_to ="blogs")


    def __str__(self) -> str:
        return self.title
