from django.db import models

class GoGame(models.Model):
    sgf_file = models.FileField(upload_to='sgf')