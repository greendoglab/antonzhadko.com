from django.conf import settings
from django.contrib.sites.models import Site
from models import Menu, Meta, SiteTitle, MyPhoto
from filmd.blog.models import Tag
from django.db.models import Avg, Max, Min, Count

def myphoto(request):
    return {
        'myphoto' : MyPhoto.objects.all()[:1],
    }

def site_menu(request): 
    return {
        'site_menu' : Menu.objects.all(),
    }

def site_meta(request):
    return {
        'site_title' : SiteTitle.objects.all()[:1],
        'site_meta' : Meta.objects.all()[:1],
    }

def site_tags(request):
    return {
        'tags' : Tag.objects.annotate(num_post=Count('post')).filter(num_post__gte=1)
    }

def current_site(request):
    try:
        current_site = Site.objects.get_current()
        return {'current_site': current_site}
    except Site.DoesNotExist:
        return {'current_site': ''}