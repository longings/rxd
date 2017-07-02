import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, User
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.fields import ThumbnailerImageField
from utils import upload

# TBI_DIR = os.path.join(upload, settings.THUMBNAIL_BASEDIR)


class RxdUserManager(UserManager):
    def _create_user(self, username, email, password, user_type=None, **extra_fields):

        if not username:
            raise ValueError('The given username must be set')

        tp = {1: 'Personal User', 2: 'Company', 3: 'Media', 4: 'Government', 5: 'Education or Community'}
        for k in tp:
            print(str(k) + ':' + tp[k])
        user_type = input(_("What type of the account fits you: "))
        user_type = int(user_type)

        phone = input(_("what is you mobile phone Number: "))
        phone = int(phone)

        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        #user = self.model(username=username, email=email, **extra_fields)
        user = self.model(username=username, email=email, phone=phone, user_type=user_type, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, phone=None, user_type=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(username=username, email=email, phone=phone, user_type=user_type, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(username, email, password, **extra_fields)

    def get_queryset(self):
        return super(RxdUserManager, self).get_queryset()
        # return super(RxdUserManager, self).get_gueryset().filter(pk__lte=100)

    def get_by_natural_key(self, email):
        return self.get(**{self.model.USERNAME_FIELD: email})

class RxdUser(AbstractUser):
    USER_TYPE = {
        (1, _('Personal User')),
        (2, _('Company')),
        (3, _('Media')),
        (4, _('Government')),
        (5, _('Community & Educations')),
    }
    email = models.EmailField(_('email address'), unique=True, blank=False)
    user_type = models.PositiveSmallIntegerField(_('user type'), choices=USER_TYPE, blank=False, null=False)
    phone = models.IntegerField(_('mobile phone'), null=False, blank=False)

    #rxdManager = RxdUserManager()
    objects = RxdUserManager()
    #USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return '%s' % self.username

    def get_full_name(self):
        return '%s•%s' % (self.first_name, self.last_name)  # English

    def get_short_name(self):
        return '%s' % self.first_name


class Profile(models.Model):

    GENDER = (
        (1, _('Male')),
        (2, _('Female')),
    )

    AVATAR_SETTINGS = {
        'size': (settings.AVATAR_SIZE, settings.AVATAR_SIZE),
        'crop': settings.AVATAR_CROP,
        'quality': settings.AVATAR_QUALITY,
        'subsampling': settings.AVATAR_SUBSAMPLING,
        'HIGH_RESOLUTION': True
    }

    user    = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True, verbose_name=_('name'))
    gender  = models.PositiveSmallIntegerField(_('gender'), choices=GENDER, null=False, blank=False)
    avatar  = ThumbnailerImageField(_('avatar'), null=False, resize_source=AVATAR_SETTINGS)
    birth_date  = models.DateTimeField(_('birth date'), null=False, blank=False)
    background  = models.ImageField(_('background'), upload_to=upload, null=True, blank=True)
    college     = models.CharField(_('college'), max_length=23, null=True, blank=True)
    city        = models.CharField(_('city'), max_length=23, null=True, blank=True)
    job         = models.CharField(_('job'), max_length=23, null=True, blank=True)
    descriptione= models.CharField(_('descriptione'), max_length=666, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return "%s%s" % (self.user.last_name, self.user.first_name)

    def get_en_name(self):
        return self.user.get_full_name()

    @property
    def age(self):
        if not self.birth_date:
            return False
        else:
            today = timezone.now()
            age = today.year - self.birth_date.year

        return '%s' % age

    def get_age(self):
        return '%s' % self.age

    # class ThirdUser(models.Model):
    #     user_id = models.CharField(blank=False)
    #     token = models.CharField()
    #     weibo = models.CharField()
    #     weixin = models.CharField()
    #
