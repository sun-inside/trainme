from tastypie import fields, utils
from tastypie.resources import ModelResource
from coach.models import Coach, Event, Place, Sportsmen


class CoachResource(ModelResource):
    class Meta:
        queryset = Coach.objects.all()
        resource_name = 'coach'

class PlaceResource(ModelResource):
    class Meta:
        queryset = Place.objects.all()
        resource_name = 'place'

class EventResource(ModelResource):
    coach = fields.ForeignKey(CoachResource, 'coach', blank=True, null=True)
    place = fields.ForeignKey(PlaceResource, 'place', blank=True, null=True)
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'



class SportsmenResource(ModelResource):
    event = fields.ManyToManyField(EventResource, 'event', blank=True, null=True)
    class Meta:
        queryset = Sportsmen.objects.all()
        resource_name = 'sportsmen'