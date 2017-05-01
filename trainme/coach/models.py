from django.db import models

class Coach(models.Model):
    name = models.CharField(max_length=32)
    club = models.CharField(max_length=32)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __unicode__(self):
        return self.name + ' (' + self.club + ')'


class Event(models.Model):
    title = models.CharField(max_length=64)
    coach = models.ForeignKey(Coach, blank=False, null=False)
#    start_time = models.CharField(max_length=64)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __unicode__(self):
        return self.title + ' (' + self.coach.name + ')'
