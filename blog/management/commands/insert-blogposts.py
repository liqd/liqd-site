# -*- coding: utf-8 -*-
import urllib2

from datetime import date
from datetime import timedelta
from datetime import datetime
from time import strftime
from BeautifulSoup import BeautifulSoup

from django.conf import settings
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import smart_str, smart_unicode

from blog.models import *


class Command(BaseCommand):
    help = u'Collects all Blogposts from the old websites and imports to new website'

    def enumerate_month_dates(self, start_date, end_date):
        current = start_date
        while current <= end_date:
            if current.month >= 12:
                next = date(current.year + 1, 1, 1)
            else:
                next = date(current.year, current.month + 1, 1)
            last = min(next - timedelta(1), end_date)
            yield current, last
            current = next

    def handle(self, *args, **options):
        start_date = date(2009, 9, 1)
        end_date = date.today()

        generator = self.enumerate_month_dates(start_date, end_date)
        months = {
            'Januar': 1,
            'Februar': 2,
            'März': 3,
            'April': 4,
            'Mai': 5,
            'Juni': 6,
            'Juli': 7,
            'August': 8,
            'September': 9,
            'Oktober': 10,
            'November': 11,
            'Dezember': 12
        }
        links = []

        for i in generator:
            url = "http://liqd.net/" + i[0].strftime("%Y/%m/")

            try:
                opener = urllib2.build_opener()
                opener.addheaders = [('User-agent', 'Mozilla/5.0')]
                response = opener.open(url)
                soup = BeautifulSoup(response)
                headers = soup.findAll("h2", {"class": "entry-title"})
                for header in headers:
                    link = header.findChildren('a')[0]['href']
                    print link
                    links.append(link)
            except:
                pass

        blog_index = BlogIndexPage.objects.first()

        for index, link in enumerate(links):
            opener = urllib2.build_opener()
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            response = opener.open(link)
            soup = BeautifulSoup(response)
            title = soup.findAll("h1", {"class": "entry-title"})
            title = smart_str(title[0].string)
            entry_date = soup.findAll("span", {"class": "entry-date"})
            entry_date = entry_date[0].string.replace(".", "").split(" ")
            entry_date = date(
                int(entry_date[2]), months[entry_date[1].encode('utf8')], int(entry_date[0]))
            entry_date = entry_date
            text = soup.findAll("div", {"class": "entry-content"})
            text = text[0].findChildren("p")
            result = ""
            for t in text:
                result = result + smart_str(str(t))

            slug = slugify(title)[:50] + str(index)
            page = BlogPage(
                title=title, date=entry_date, body=result, slug=slug)
            blog_index.add_child(instance=page)
