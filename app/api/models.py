from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from . import mixins
from .services import domain


class Test(mixins.UUIDMixin):
    login = models.CharField(max_length=10, unique=True, default=domain.create_login)
    created_at = models.DateTimeField(auto_now_add=True)


class IQTest(mixins.UUIDMixin, mixins.TestFieldsMixin):
    test = models.OneToOneField(Test, on_delete=models.CASCADE)
    result = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(0),
                                                                    MaxValueValidator(50)])


class EQTest(mixins.UUIDMixin, mixins.TestFieldsMixin):
    test = models.OneToOneField(Test, on_delete=models.CASCADE)
    result = ArrayField(models.CharField(max_length=1, blank=False,  null=False), size=5)
