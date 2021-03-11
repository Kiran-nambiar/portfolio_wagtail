from __future__ import unicode_literals
import graphene
from graphene_django import DjangoObjectType
from about.models import AboutPage
from work.models import WorkPage

from django.db import models
from api import graphene_wagtail

class AboutNode(DjangoObjectType):
    class Meta:
        model = AboutPage
        only_fields = ['id', 'title', 'content', 'side_image']


class Query(graphene.ObjectType):
    about = graphene.List(AboutNode)

    @graphene.resolve_only_args
    def resolve_about(self):
        return AboutPage.objects.live()

schema = graphene.Schema(query=Query)

class WorkNode(DjangoObjectType):
    class Meta:
        model = WorkPage
        only_fields = ['id', 'work_title']


class Query(graphene.ObjectType):
    work = graphene.List(WorkNode)

    @graphene.resolve_only_args
    def resolve_about(self):
        return WorkPage.objects.live()

schema = graphene.Schema(query=Query)