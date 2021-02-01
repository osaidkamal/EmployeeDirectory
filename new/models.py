from django.db import models
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have username")
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
 
class myuser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(
        verbose_name="last login", auto_now_add=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def _str_(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Detail(models.Model):
    fullname=models.CharField(max_length=20,default="")
    image = models.ImageField(null=True, blank=True)
    desc = models.TextField(max_length=500, default="")
    shdesc = models.TextField(max_length=30, default="")
    name = models.OneToOneField(myuser, default=None,
                             on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
