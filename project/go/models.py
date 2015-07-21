from django.contrib.auth.models import AbstractUser
from django.db import models


class GoUser(AbstractUser):
    pass

class GoGame(models.Model):
    sgf_file = models.FileField(upload_to='sgf')