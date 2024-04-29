import uuid
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Emailは必ず必要です")
        if not username:
            raise ValueError("Usernameは必ず必要です")

        if not password:
            raise ValueError("Passwordは必ず必要です")

        # extra_fields.setdefault("is_active", True)

        user = self.model(
            email=self.normalize_email(email), username=username, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username, password=None, **extra_fields):
        user = self.create_user(
            email,
            username=username,
            password=password,
            **extra_fields,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(
            email,
            password=password,
            **extra_fields,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)

    email = models.EmailField(
        verbose_name="Eメールアドレス",
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
            "validators": "この項目は必須です。全角文字、半角英数字、@/./+/-/_ で50文字以下にしてください。",
        },
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.admin

    def has_module_perms(self, app_label):
        return self.admin

    # @property
    # def is_staff(self):
    #     return self.is_staff

    @property
    def admin(self):
        return self.is_superuser

    @property
    def active(self):
        return self.is_active
