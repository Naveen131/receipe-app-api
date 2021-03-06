from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**extrafields):
        if not email:
            raise ValueError("Users must have email")
        user = self.model(email=self.normalize_email(email),**extrafields)
        user.set_password(password)
        user.save(self._db)
        return user


    def create_superuser(self,email,password=None,**extrafields):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects= UserManager()

    USERNAME_FIELD = "email"
