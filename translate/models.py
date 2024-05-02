from django.db import models

# Create your models here.

# class Translate(models.Model):
#     text = models.TextField()
#     target_language = models.CharField(max_length=10)

class Stars(models.Model):
    full_name = models.CharField(max_length=30)
    phone = models.EmailField(max_length=10)
    stars = models.IntegerField(null=True, blank=True)
    comment = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.full_name}  {self.stars} - yulduzcha qo'ydi"

# class Quetions(models.Model):
#     quetions = models.CharField(max_length=30)
#     answer = models.TextField(help_text="Javob")

#     def __str__(self):
#         return f"{self.quetions} - {self.answer}"


