from tastypie import fields, utils
from tastypie.resources import ModelResource
from coach.models import Coach, Event


class CoachResource(ModelResource):
    class Meta:
        queryset = Coach.objects.all()
        resource_name = 'coach'


class EventResource(ModelResource):
    coach = fields.ForeignKey(CoachResource, 'coach', blank=True, null=True)
    class Meta:
        queryset = Event.objects.all()
        resource_name = 'event'
