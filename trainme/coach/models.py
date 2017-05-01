from django.db import models


sport_type =["SKI","RUN","BIKE","SWIM"]

SPORT_TYPE = (
        ('SKI', 'Cross country skiing'),
        ('RUN', 'Running'),
        ('BIKE', 'Bicycling'),
        ('SWIM', 'Swimming')
    )

class Coach(models.Model):
    name = models.CharField(max_length=32)
    club = models.CharField(max_length=32)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    sport_type = models.CharField(max_length=1, choices=SPORT_TYPE )

    def __unicode__(self):
        return self.name + ' (' + self.club + ')'

class Place(models.Model):
    title = models.CharField(max_length=64)
    geo_lat = models.FloatField()
    geo_lon = models.FloatField()
    address = models.TextField()

class Event(models.Model):
    title = models.CharField(max_length=64)
    coach = models.ForeignKey(Coach, blank=False, null=False)
    place = models.ForeignKey(Place, blank=False, null=False)
    ##visitors = models.ManyToManyField(Sportsmen)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    description = models.TextField()

    def __unicode__(self):
        return self.title + ' (' + self.coach.name + ')'


class Sportsmen(models.Model):
    name = models.CharField(max_length=32)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    sport_type = models. CharField(max_length=1, choices=SPORT_TYPE )

    event = models.ManyToManyField(Event)
