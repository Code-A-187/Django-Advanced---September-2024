from django.contrib.auth.models import AbstractUser, User
from django.db import models


class CustomUser(AbstractUser):
    points = models.IntegerField(
        default=0
    )


class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE
    )
    age = models.IntegerField()

    first_name = models.CharField(
        max_length=30
    )

    last_name = models.CharField(
        max_length=30
    )

    points = models.IntegerField(
        default=0
    )


# class CustomProxyModel(CustomUser):
#
#     def custom_method(self):
#         return f"This is a custom method"
#
#     class Meta:
#         proxy = True
#
#
# print(CustomUser.custom_method())
# print(CustomProxyModel.custom_method())
