from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model for django project"""

    class Meta:
        db_table = 'dd_users'

    def __str__(self) -> str:
        return self.username