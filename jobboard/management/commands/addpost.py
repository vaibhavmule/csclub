import os
import wxr_parser

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.redirects.models import Redirect
from django.contrib.sites.models import Site
from django.conf import settings
from blog.models import Post


class Command(BaseCommand):
    help = 'Add blog posts to CSClub'

    def handle(self, *args, **options):
        pwd = os.path.dirname(__file__)
        parsed_data = wxr_parser.parse(pwd + '/wordpress.xml')
        site = Site.objects.get(pk=settings.SITE_ID)
        for post in parsed_data['posts']:
            if post['status'] and post['title'] and post['slug']:
                username = post['creator']
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user = User(username=username)
                    user.save()
                post_obj = Post(
                    author=user,
                    slug=post['slug'],
                    title=post['title'],
                    text=post['content'],
                    published_date=post['pub_date'])
                post_obj.save()
                Redirect.objects.create(
                    site=site,
                    old_path='/blog/' + post['slug'] + '/',
                    new_path='/' + username + '/' + post_obj.slug + '/')
                self.stdout.write(self.style.SUCCESS('ok'))
