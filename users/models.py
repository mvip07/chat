from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class UserModel (models.Model):
    bio = models.CharField(name='bio', max_length=80)
    id = models.AutoField(name='id', primary_key=True)
    block = models.BooleanField(name='block', default=False)
    last_name = models.CharField(name='last_name', max_length=70)
    first_name = models.CharField(name='first_name', max_length=70)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    username = models.CharField(name='username', max_length=70, unique=True)
    phone = models.CharField(name='phone', max_length=30, blank=False, unique=True)
    image = models.ImageField(upload_to='image')
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(100, 50)],
        format='JPEG',
        options={'quality': 60}
    )

    def __str__(self) -> str:
        return str(self.id)

    def get_absolute_url (self):
        return reverse('login')

class MessageModel (models.Model):
    message = models.TextField(name='message')
    id = models.AutoField(name='id', primary_key=True)
    block = models.BooleanField(name='block', default=False)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    to_id = models.ForeignKey('UserModel', related_name ='to_id', on_delete=models.CASCADE)
    from_id = models.ForeignKey('UserModel', related_name ='from_id', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.id)

    def get_absolute_url (self):
        return reverse('login')