from django.db import models
from ckeditor.fields import RichTextField

class EducationDegreeChoices(models.TextChoices):
    MASTER = "master", "Magistratura"
    BACHELORS = "bachelors", "Bakalavr"


class LanguageChoices(models.TextChoices):
    UZ = "uz", "O'zbek tili"
    RU = "ru", "Rus tili"
    EN = "en", "Ingiliz tili"


class EducationTypeChoices(models.TextChoices):
    DAYTIME = "daytime", "Kunduzgi"
    PART_TIME = "part_time", "Sirtqi"
    EVENING = "evening", "Kechki"


class Director(models.Model):
    full_name = models.CharField(max_length=150)
    bio = RichTextField()
    phone_number = models.CharField(max_length=15)
    picture = models.ImageField(upload_to="images")

    def __str__(self):
        return self.full_name



class Faculty(models.Model):
    title = models.CharField(max_length=20)
    body = RichTextField()
    degree = models.CharField(max_length=20, choices=EducationDegreeChoices.choices)
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"




class Direction(models.Model):
    title = models.CharField(max_length=20)
    language = models.CharField(max_length=20, choices=LanguageChoices.choices)
    body = RichTextField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name="directions")
    education_type = models.CharField(max_length=20, choices=EducationTypeChoices.choices)

    def __str__(self):
        return self.title