from django.db import models

class TimeZonePreference(models.Model):
    name = models.CharField(max_length=100)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.timezone}"
