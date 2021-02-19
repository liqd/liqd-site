import json
from datetime import date, timedelta
from urllib.request import urlopen

import bleach
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from apps.blog.models import BlogIndexPage, BlogPage


class Command(BaseCommand):
    help = u'Collects all Blogposts'
    ' from the old websites and imports to new website'

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
            url = "https://www-wp.liqd.net/" + i[0].strftime("%Y/%m/")

            try:
                response = urlopen(url)
                response.addheaders = [('User-agent', 'Mozilla/5.0')]
                soup = BeautifulSoup(response)
                headers = soup.findAll("h2", {"class": "entry-title"})
                for header in headers:
                    link = header.findChildren('a')[0]['href']
                    links.append(link)
            except Exception:
                pass

        blog_index = BlogIndexPage.objects.first()

        for index, link in enumerate(links):
            response = urlopen(link)
            response.addheaders = [('User-agent', 'Mozilla/5.0')]
            soup = BeautifulSoup(response)
            title = soup.findAll("h1", {"class": "entry-title"})
            title = str(title[0].string)
            entry_date = soup.findAll("span", {"class": "entry-date"})
            entry_date = entry_date[0].string.replace(".", "").split(" ")

            entry_date = date(
                int(entry_date[2]), months[entry_date[1]], int(entry_date[0]))
            entry_date = entry_date
            text = soup.findAll("div", {"class": "entry-content"})
            text = text[0].findChildren("p")
            result = ""
            for t in text:
                result = result + str(str(t))

            result = result + '<a href="' + link + '">' + link + '</a>'

            clean_result = bleach.clean(result,
                                        tags=[],
                                        attributes={},
                                        styles=[],
                                        strip=True
                                        )
            subtitle_en = clean_result[0:100]
            intro_en = clean_result[0:100]
            title_en = title
            result = [
                {'type': 'paragraph', 'value': result

                 }]

            result = json.dumps(result, ensure_ascii=False)

            slug = slugify(title)[:50] + str(index)
            try:
                page = BlogPage(
                    title=title,
                    live=False,
                    date=entry_date,
                    body_en=result,
                    title_en=title_en,
                    subtitle_en=subtitle_en,
                    intro_en=intro_en,
                    slug=slug)
                blog_index.add_child(instance=page)
            except Exception:
                pass
