from django.db import models
from django.core.exceptions import ValidationError


def validate_stars(value):
    if value > 5 or value < 1:
        raise ValidationError(
            "Rating must be between 1 and 5",
            params={"value": value},
        )
    

class Stars(models.Model):
    full_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    stars = models.IntegerField(validators=[validate_stars], null=True, blank=True)
    comment = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.full_name}  {self.stars} - yulduzcha qo'ydi"


class FAQ(models.Model):
    full_name = models.CharField(max_length=30)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=500, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name}  {self.question}"
