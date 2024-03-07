from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    #used to manipulate objects
    def create_user(self,email,name,password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')
        
        #normalising email address
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)# encypts the pass   hashed pass
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,name,password):
        """create and save a new super user with given details"""
        user=self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email=models.EmailField(max_length=255, unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True) # this allows us to deactivate users when needed
    is_staff=models.BooleanField(default=False)# this allows us to make any user a staff memeber

    objects=UserProfileManager()

    USERNAME_FIELD = 'email' 
     #here we are overriding the default uname field with our email field
     #This is added to work with the Django Admin and also the Django authentication system
    REQUIRED_FIELDS=['name']



    #used for django to interact with our umodel
    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self):
        """Retrieve short name of user"""
        return self.name
    
    #string representation of our umodel

    def __str__(self):
        """Return string representation of our umodel"""
        return self.email



