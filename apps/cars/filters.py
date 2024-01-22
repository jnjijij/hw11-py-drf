from django.db.models import QuerySet
from django.http import QueryDict
from rest_framework.exceptions import ValidationError

from .models import CarModel


def cars_filter(query: QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'brand_end':
                qs = qs.filter(brand__iendswith=v)
            case _:
                raise ValidationError({'Details': f'{k} is not a allowed here'})
    return qs
