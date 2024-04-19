from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from cms.accounts.managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _("email"),
        unique=True,
        error_messages={
            "unique": _("This email already exists! Please choose another one."),
        },
    )

    date_joined = models.DateTimeField(
        _("date joined"),
        default=timezone.now),

    is_active = models.BooleanField(
        _("active"),
        default=True,
    )

    is_staff = models.BooleanField(
        _("staff"),
        default=False,
    )

    USERNAME_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email.split('@')[0]


# regular user profile
class Profile(models.Model):
    first_name = models.CharField(
        _("first name"),
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        _("last name"),
        max_length=30,
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        _("phone number"),
        max_length=20,
        blank=True,
        null=True,
    )

    profile_picture = models.ImageField(
        _("profile picture"),
        upload_to="profile_pictures/",
        blank=True,
        null=True,
    )

    city = models.CharField(
        _("city"),
        max_length=50,
        blank=True,
        null=True,
    )

    postal_code = models.CharField(
        _("postal code"),
        max_length=20,
        blank=True,
        null=True,
    )

    street = models.CharField(
        _("street"),
        max_length=100,
        blank=True,
        null=True,
    )

    address_info = models.CharField(
        _("address info"),
        max_length=100,
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        User,
        primary_key=True,
        related_name="user_profile",
        on_delete=models.CASCADE,
    )
