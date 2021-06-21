from django.db import models

# Create your models here.

class Applessons(models.Model):
    name_lessons = models.CharField(max_length=70)
    teacher_name = models.CharField(max_length=80)

    def __str__(self):
        return self.name_lessons
