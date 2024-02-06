from django.core import validators as V
from django.db import models

from apps.cars.choises.body_type_choices import BodyTypeChoices
from core.enums.regex_enum import Regex
from core.models import BaseModel

from apps.auto_parks.models import AutoParkModel
from apps.cars.managers import CarManager
from core.services.file_service import FileService


class CarModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ['-id']

    brand = models.CharField(max_length=20, validators=[V.RegexValidator(*Regex.BRAND.value)])
    price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(100_000)])
    year = models.IntegerField()
    body_type = models.CharField(max_length=9, choices=BodyTypeChoices.choices)
    photo = models.ImageField(upload_to=FileService.upload_car_photo, blank=True)

    objects = CarManager()
