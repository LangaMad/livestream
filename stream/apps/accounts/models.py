from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)



from ..streams.models import Stream
class User(AbstractUser):
    username = models.CharField('Никнейм',max_length=50, unique=True)
    email = models.EmailField('Почта', unique=True)
    avatar = models.ImageField('Аватар', upload_to='avatars/',
    null=True, blank=True)
    status = models.CharField('Статус', max_length=100, null=True, blank=True)
    download_games = models.ManyToManyField('games.Games', blank=True,related_name='download_games')
    friends_online = models.ManyToManyField('self',  blank=True)
    live_streams = models.ManyToManyField('streams.Stream', blank=True, related_name='live_streams')
    clips = models.ManyToManyField('streams.Stream', blank=True, related_name='clips')


    objects = UserManager()



