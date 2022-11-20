from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File
# Create your models here.

class blog(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    profile = models.ImageField(upload_to = 'images/blogs',null=True)
    created_date =models.DateField(auto_now=True, blank=False, null=False)
    updated_date = models.DateField(auto_now=False, blank=True, null=True)

class profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic =  models.ImageField(upload_to='images')  

    # compress image

    # before saving the instance we’re reducing the image
    def save(self, *args, **kwargs):
        new_image = self.reduce_image_size(self.profile_pic)
        self.profile_pic = new_image
        super().save(*args, **kwargs)

    def reduce_image_size(self, profile_pic):
        print(profile_pic)
        img = Image.open(profile_pic)
        thumb_io = BytesIO()
        img.save(thumb_io, 'jpeg', quality=50)
        new_image = File(thumb_io, name=profile_pic.name)
        return new_image
    