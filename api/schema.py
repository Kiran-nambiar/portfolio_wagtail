from __future__ import unicode_literals
import graphene
from graphene_django import DjangoObjectType
from about.models import AboutPage
from work.models import WorkPage, TechnologyPage, TechnologyDetailOrderable
from home.models import HomePage, HomeSelectionOrderable
from about.models import AboutPage, DeveloperLogo
from contact.models import FormField, ContactPage
from wagtail.core.models import Page
from itertools import chain
from django.db import models
from api import graphene_wagtail

class PageModel(DjangoObjectType):
    
    class Meta:
        model = Page

# ==================== This is for Home Page =================================================

class HomeNode(DjangoObjectType):
    class Meta:
        model = HomeSelectionOrderable

class HomeOrderableNode(DjangoObjectType):
    class Meta:
        model = HomePage

class HomeAssetUnion(graphene.types.Union):
    class Meta:
        types = [HomePage, HomeSelectionOrderable]

class HomeParentNode(graphene.ObjectType):
    assets = graphene.Field(HomeAssetUnion)
    def resolve_assets(self, info):
        return list(chain(HomePage.objects.all(), HomeSelectionOrderable.objects.all()))


# ==================== This is for About Page =================================================


class AboutOrderableNode(DjangoObjectType):
    class Meta:
        model = DeveloperLogo

class AboutNode(DjangoObjectType):
    class Meta:
        model = AboutPage

class AboutAssetUnion(graphene.types.Union):
    class Meta:
        types = [AboutPage, DeveloperLogo]

class AboutParentNode(graphene.ObjectType):
    assets = graphene.Field(AboutAssetUnion)
    def resolve_assets(self, info):
        return list(chain(AboutPage.objects.all(), DeveloperLogo.objects.all()))


# ==================== This is for Work Page =================================================


class TechnologyDetailOrderableNode(DjangoObjectType):
    class Meta:
        model = TechnologyDetailOrderable

class TechnologyWorkNode(DjangoObjectType):
    class Meta:
        model = TechnologyPage


class WorkAssetUnion(graphene.types.Union):
    class Meta:
        types = [TechnologyPage, TechnologyDetailOrderable]

class WorkParentNode(graphene.ObjectType):
    assets = graphene.Field(WorkAssetUnion)
    
    def resolve_assets(self, info):
        return list(chain(TechnologyPage.objects.all(), TechnologyDetailOrderable.objects.all()))

class FullStackWorkNode(DjangoObjectType):
    technology = graphene.List(PageModel)
    class Meta:
        model = WorkPage
    
    def resolve_technology(self, info):
        return self.get_children()


# ==================== This is for Contact Page =================================================


class ContactNode(DjangoObjectType):
    class Meta:
        model = ContactPage

class ContactFormNode(DjangoObjectType):
    class Meta:
        model = FormField

class ContactAssetUnion(graphene.types.Union):
    class Meta:
        types = [ContactPage, FormField]

class ContactParentNode(graphene.ObjectType):
    assets = graphene.Field(ContactAssetUnion)
    def resolve_assets(self, info):
        return list(chain(ContactPage.objects.all(), FormField.objects.all()))

        
class Query(graphene.ObjectType):
    about = graphene.List(AboutNode)
    work = graphene.List(FullStackWorkNode)
    homepage = graphene.List(HomeOrderableNode)
    contact = graphene.List(ContactNode)

    def resolve_about(self, arg):
        return AboutPage.objects.all()

    def resolve_work(self, arg):
        return WorkPage.objects.all()
    
    def resolve_homepage(self, arg):
        return HomePage.objects.all()

    def resolve_contact(self, arg):
        return ContactPage.objects.all()

    
schema = graphene.Schema(query=Query)