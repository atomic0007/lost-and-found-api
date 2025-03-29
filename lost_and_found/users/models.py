from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add additional fields like profile_picture if needed
    pass

