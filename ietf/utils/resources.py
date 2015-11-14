# Autogenerated by the mkresources management command 2014-11-13 05:39
from tastypie.resources import ModelResource
from tastypie.fields import CharField

from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from ietf import api

class UserResource(ModelResource):
    username = CharField()
    class Meta:
        queryset = User.objects.all()
        serializer = api.Serializer()

class ContentTypeResource(ModelResource):
    username = CharField()
    class Meta:
        queryset = ContentType.objects.all()
        serializer = api.Serializer()

        


class DumpInfoResource(ModelResource):
    class Meta:
        queryset = DumpInfo.objects.all()
        serializer = api.Serializer()
        #resource_name = 'dumpinfo'
        filtering = { 
            "id": ALL,
            "date": ALL,
            "host": ALL,
        }
api.utils.register(DumpInfoResource())

