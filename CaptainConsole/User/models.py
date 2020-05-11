from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=9999, default="https://previews.123rf.com/images/alekseyvanin/alekseyvanin1704/alekseyvanin170403722/76700719-user-line-icon-profile-outline-vector-logo-illustration-linear-pictogram-isolated-on-white.jpg")
