from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import uuid


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, government_id, mobile_number, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, government_id=government_id, mobile_number=mobile_number,
                          **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email='admin@globalfarmer.com', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email=email, password=password, full_name='super user', mobile_number='+1234567890', **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'government_id'

    class Countries(models.TextChoices):
        TANZANIA = 'TZ', _('Tanzania')
        KENYA = 'KE', _('Kenya')
        NIGERIA = 'NG', _('Nigeria')
        ETHIOPIA = 'ET', _('Ethiopia')
        SOUTH_AFRICA = 'ZA', _('South Africa')
        UGANDA = 'UG', _('Uganda')
        RWANDA = 'RW', _('Rwanda')
        BURUNDI = 'BI', _('Burundi')
        ZAMBIA = 'ZM', _('Zambia')
        ZIMBABWE = 'ZW', _('Zimbabwe')
        MALAWI = 'MW', _('Malawi')

    class UserChoice(models.TextChoices):
        FARMER = 'FARMER', _('Farmer')
        BUYER = 'BUYER', _('Buyer')
        INSPECTOR = 'INSPECTOR', _('Inspector')

    class RegisteredChoices(models.TextChoices):
        YES = 'YES', _('Yes')
        NO = 'NO', _('No')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100)
    government_id = models.CharField(max_length=50, unique=True)
    user_type = models.CharField(blank=True, choices=UserChoice.choices, default=UserChoice.FARMER, max_length=10)
    mobile_number = models.CharField(max_length=15)
    device_used = models.CharField(max_length=30, default='Desktop-Windows_11')
    country = models.CharField(max_length=4,
                               choices=Countries.choices,
                               default=Countries.TANZANIA
                               )
    email = models.EmailField(blank=True, null=True)
    location = models.CharField(max_length=80, help_text='Street or village')
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    password = models.CharField(_('password'), max_length=128, null=False)
    last_login = models.DateTimeField(auto_now=True)
    is_registered = models.CharField(max_length=4,
                                     choices=RegisteredChoices.choices,
                                     default=RegisteredChoices.NO)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name}"

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
