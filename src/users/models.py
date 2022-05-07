from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid


class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        abstract = False

    class Genders(models.TextChoices):
        MALE = 'male', _('Male')
        FEMALE = 'female', _('Female')

    gender = models.CharField(_('Gender'), max_length=12, choices=Genders.choices, blank=True)
    uuid = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def printable_gender(self):
        return self.gender or 'Unknown Gender'
