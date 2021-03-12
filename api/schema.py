from __future__ import unicode_literals
import graphene
from graphene_django import DjangoObjectType
from about.models import AboutPage
from work.models import FullStackPage, TechnologyPage
from wagtail.core.models import Page

from django.db import models
from api import graphene_wagtail

class PageModel(DjangoObjectType):
    
    class Meta:
        model = Page
class AboutNode(DjangoObjectType):
    class Meta:
        model = AboutPage
        only_fields = ['id', 'title', 'content', 'side_image']

class TechnologyWorkNode(DjangoObjectType):
    class Meta:
        model = TechnologyPage
        only_fields = ['id', 'title', 'software_title']

class FullStackWorkNode(DjangoObjectType):
    technology = graphene.List(PageModel)
    class Meta:
        model = FullStackPage
        only_fields = ['id', 'title', 'description']
    
    def resolve_technology(self, info):
        return self.get_children()
        
class Query(graphene.ObjectType):
    about = graphene.List(AboutNode)
    full_stack = graphene.List(FullStackWorkNode)

    def resolve_about(self, arg):
        return AboutPage.objects.all()

    def resolve_full_stack(self, arg):
        return FullStackPage.objects.all()
        
schema = graphene.Schema(query=Query)