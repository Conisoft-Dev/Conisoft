from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, User
)

# user with foriegn key
class Attendee(models.Model):
    Full_Name = models.CharField(max_length=200)
    industry_type = models.CharField(max_length=200)
    presenter = models.BooleanField(default=False)
    reciept = models.FileField()
    guest = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) # Foriegn Key to default user class

    def __str__(self):
        return self.name


# Main Workshop Model
class Worshop(models.Model):
    name = models.CharField(max_length=200)
    presenter = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    date = models.DateTimeField()
    open_slots = models.IntegerField()
    taken_slots = models.IntegerField(default=0)
    zoom_link = models.CharField(blank=True, max_length=500)

    def __str__(self):
        return self.name

# Home page Carosel
class Carosel(models.Model):
    heading = models.CharField(max_length=200)
    text = models.CharField(max_length=500)
    background_image = models.URLField()
    logo = models.URLField()

    def __str__(self):
        return self.heading

# Topics below Carosel
class Topic(models.Model):
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=500)

    def __str__(self):
        return self.name

# Call For Papers
class PaperRequirement(models.Model):
    heading = models.CharField(max_length=200)

    def __str__(self):
        return self.heading

class Bullet(models.Model):
    heading = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    Paper_requirement = models.ForeignKey(PaperRequirement, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.heading

# Display courses (Workshops)
class Course(models.Model):
    date = models.DateField()
    time_length = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    presenter = models.CharField(max_length=200)
    image = models.URLField()
    presenter_image = models.URLField()

    def __str__(self):
        return "course: %s presenter: %s" %(self.name, self.presenter)

# Previous additions

class Edition(models.Model):
    year = models.CharField(max_length=4)
    image = models.URLField()
    link = models.URLField()

    def __str__(self):
        return "conisoft %s" % self.year



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
    reciept = models.FileField()
    guest = models.IntegerField(default=0)


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


