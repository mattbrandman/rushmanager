from django.db import models
from django.contrib.auth.models import User, PermissionsMixin
from organization.models import Organization
from django.contrib.auth.models import Permission, AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.db import connection
from django.conf import settings
from tenancy.models import TenantAware
from django.contrib.postgres.fields import HStoreField


class BrotherUserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_created=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class BrotherUser(AbstractBaseUser, PermissionsMixin, TenantAware):
    email = models.CharField(max_length=100, unique=True)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_created = models.DateTimeField(default=timezone.now, blank=True)
    is_active = models.BooleanField(default=True)
    organization = models.ForeignKey('organization.Organization')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = BrotherUserManager()

    def get_full_name():
        return first_name + " " + last_name

    def get_short_name():
        return first_name


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="profile")
    ranking = models.ManyToManyField('ranking.Ranking')
    class Meta:
        permissions = (
            ("chapter_admin", "Can access chapter admin page"),
        )

    def __str__(self):
        return self.user.username
