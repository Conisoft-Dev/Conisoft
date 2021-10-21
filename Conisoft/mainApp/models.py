from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


# Home page Carosel
class Carosel(models.Model):
    heading = models.CharField(max_length=200)
    text = models.CharField(max_length=450)
    background_image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)
    logo_image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, default='path/to/my/default/image.jpg')


    def __str__(self):
        return self.heading


class Course(models.Model):
    date = models.DateField()
    time = models.TimeField()
    time_length = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, default="course@mail.com")
    description = models.CharField(max_length=200)
    presenter = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, default="None/conisoft_logo_0SeqbbO.png")
    presenter_image = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100)
    attendants = models.IntegerField(default=0)
    max_size = models.IntegerField(default=20)
    zoom_link = models.CharField(blank=True, max_length=500)
    approved = models.BooleanField(default=False) # reciept approval

    context_object_name = 'Course'
    def __str__(self):
        return "%s by %s" %(self.name, self.presenter)

# New User Model
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):

    context_object_name = 'User'

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser

    Full_Name = models.CharField(max_length=200)
    industry_type = models.CharField(max_length=200)
    presenter = models.BooleanField(default=False)
    approved = models.BooleanField(default=False) # reciept approval

    paper = models.FileField('paper', upload_to='papers/', null=True, blank=True)
    guests = models.IntegerField(default=0, null=True)
    courses_subscribed = models.IntegerField(default=0)

    receipt_photo = models.ImageField('Receipt Photo', upload_to='receipts/', null=True, default='None')

    course_1_name = models.CharField(max_length=200, null=True, blank=True, default='None')
    course_1_id = models.IntegerField(default=0, null=True)
    course_1_link = models.CharField(max_length=200, null=True, default='None')
    # course_1_approval = models.BooleanField(default=False) # reciept approval

    # course_2_name = models.CharField(max_length=200, null=True, blank=True, default='None')
    # course_2_id = models.IntegerField(default=0, null=True)
    # course_2_link = models.CharField(max_length=200, null=True, default='None')
    # course_2_approval = models.BooleanField(default=False) # reciept approval


    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
    
    objects = UserManager()