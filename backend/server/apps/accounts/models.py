from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        email,
        username,
        first_name,
        last_name,
        phone_number,
        town,
        county,
        password=None,
    ):
        if not email:
            raise ValueError("User must have an email")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            town=town,
            county=county,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        user = self.create_user(email, username, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    username = models.CharField(verbose_name="username", max_length=255, unique=True)
    first_name = models.CharField(verbose_name="first name", max_length=255, blank=True)
    last_name = models.CharField(verbose_name="last name", max_length=255, blank=True)
    phone_number = models.CharField(
        verbose_name="phone number", max_length=255, blank=True, null=True, default=None
    )
    town = models.CharField(verbose_name="town", max_length=255, blank=True)
    county = models.CharField(verbose_name="county", max_length=255, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "username",
        "first_name",
        "last_name",
        "phone_number",
        "town",
        "county",
    ]

    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.email
