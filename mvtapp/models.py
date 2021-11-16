from django.db import models

# Create your models here.

class LectureDetail(models.Model):
    title = models.CharField(max_length=255, null=False)
    count = models.IntegerField(null=False)