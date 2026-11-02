from types import SimpleNamespace
from unittest.mock import patch

from django.test import RequestFactory
from django.test import SimpleTestCase

from apps.core.templatetags.core_tags import do_translate_url


class TranslateUrlTestCase(SimpleTestCase):
    def setUp(self):
        self.request = RequestFactory().get("/admin/pages/1/edit/preview/")

    def test_translate_url_with_page_path(self):
        with patch(
            "apps.core.templatetags.core_tags.resolve",
            return_value=SimpleNamespace(args=("projects/demo/",)),
        ):
            url = do_translate_url({"request": self.request}, "de")

        self.assertEqual(url, "/de/projects/demo/")

    def test_translate_url_with_empty_path(self):
        with patch(
            "apps.core.templatetags.core_tags.resolve",
            return_value=SimpleNamespace(args=("",)),
        ):
            url = do_translate_url({"request": self.request}, "de")

        self.assertEqual(url, "/de/")

    def test_translate_url_with_missing_path(self):
        with patch(
            "apps.core.templatetags.core_tags.resolve",
            return_value=SimpleNamespace(args=(None,)),
        ):
            url = do_translate_url({"request": self.request}, "de")

        self.assertEqual(url, "/de/")
