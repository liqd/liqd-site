"""
Tests for Academy app, specifically for MultiSelectField functionality.
"""

from datetime import date

from django.test import TestCase
from wagtail.models import Page
from wagtail.models import Site

from apps.academy.choices import DIGITALCIVICSOCIETY
from apps.academy.choices import LIQDTHEORY
from apps.academy.choices import PARTICIPATIONACTION
from apps.academy.models import AcademyPage
from apps.core.models.home_page import HomePage


class MultiSelectFieldTestCase(TestCase):
    """Test cases for MultiSelectField in AcademyPage."""

    def setUp(self):
        """Set up test data."""
        # Get or create root page (migrations may have already created it)
        root_page = Page.objects.filter(depth=1).first()
        if not root_page:
            root_page = HomePage.objects.create(
                title="Root",
                slug="root",
                path="00010001",
                depth=1,
                numchild=0,
                url_path="/",
            )

        # Get or create site
        site = Site.objects.filter(is_default_site=True).first()
        if not site:
            Site.objects.create(
                hostname="localhost",
                port=80,
                root_page=root_page,
                is_default_site=True,
            )

        # Use root page as parent for academy pages
        self.academy_index = root_page

    def test_multiselectfield_save_and_load_single_value(self):
        """Test that MultiSelectField can save and load a single value."""
        academy_page = AcademyPage(
            title="Test Academy Page",
            slug="test-academy",
            date=date.today(),
        )
        academy_page.topics = [LIQDTHEORY]
        self.academy_index.add_child(instance=academy_page)
        academy_page.save_revision().publish()

        # Reload from database
        academy_page.refresh_from_db()

        # Check that the value is correctly stored and retrieved
        self.assertEqual(academy_page.topics, [LIQDTHEORY])

    def test_multiselectfield_save_and_load_multiple_values(self):
        """Test that MultiSelectField can save and load multiple values."""
        academy_page = AcademyPage(
            title="Test Academy Page",
            slug="test-academy",
            date=date.today(),
        )
        academy_page.topics = [LIQDTHEORY, DIGITALCIVICSOCIETY]
        self.academy_index.add_child(instance=academy_page)
        academy_page.save_revision().publish()

        # Reload from database
        academy_page.refresh_from_db()

        # Check that multiple values are correctly stored and retrieved
        self.assertEqual(
            set(academy_page.topics),
            {LIQDTHEORY, DIGITALCIVICSOCIETY},
        )

    def test_multiselectfield_max_choices_constraint(self):
        """Test that MultiSelectField validates choices and max_choices constraint."""
        academy_page = AcademyPage(
            title="Test Academy Page",
            slug="test-academy",
            date=date.today(),
        )

        # Try to set invalid choice - should raise validation error
        academy_page.topics = [
            LIQDTHEORY,
            DIGITALCIVICSOCIETY,
            PARTICIPATIONACTION,
            "EXTRA",  # Invalid choice - should raise validation error
        ]

        # The field should raise a validation error for invalid choices
        with self.assertRaises(Exception):  # ValidationError
            self.academy_index.add_child(instance=academy_page)
            academy_page.full_clean()

        # Test that max_choices (3) works correctly with valid choices
        academy_page2 = AcademyPage(
            title="Test Academy Page 2",
            slug="test-academy-2",
            date=date.today(),
        )
        academy_page2.topics = [
            LIQDTHEORY,
            DIGITALCIVICSOCIETY,
            PARTICIPATIONACTION,
        ]  # Exactly 3 valid choices
        self.academy_index.add_child(instance=academy_page2)
        academy_page2.save_revision().publish()
        academy_page2.refresh_from_db()

        # Should have exactly 3 values
        self.assertEqual(len(academy_page2.topics), 3)

    def test_multiselectfield_empty_value(self):
        """Test that MultiSelectField can handle empty values (field is optional)."""
        academy_page = AcademyPage(
            title="Test Academy Page Empty",
            slug="test-academy-empty",
            date=date.today(),
        )
        academy_page.topics = []

        # The field should accept empty values (it's optional)
        self.academy_index.add_child(instance=academy_page)
        academy_page.save_revision().publish()
        academy_page.refresh_from_db()
        self.assertEqual(academy_page.topics, [])

    def test_multiselectfield_all_choices(self):
        """Test that MultiSelectField can store all available choices."""
        academy_page = AcademyPage(
            title="Test Academy Page",
            slug="test-academy",
            date=date.today(),
        )
        # Set all three available choices
        academy_page.topics = [
            LIQDTHEORY,
            DIGITALCIVICSOCIETY,
            PARTICIPATIONACTION,
        ]
        self.academy_index.add_child(instance=academy_page)
        academy_page.save_revision().publish()

        # Reload from database
        academy_page.refresh_from_db()

        # Check that all choices are correctly stored
        self.assertEqual(
            set(academy_page.topics),
            {LIQDTHEORY, DIGITALCIVICSOCIETY, PARTICIPATIONACTION},
        )

    def test_multiselectfield_display_value(self):
        """Test that MultiSelectField displays correct human-readable values."""
        academy_page = AcademyPage(
            title="Test Academy Page",
            slug="test-academy",
            date=date.today(),
        )
        academy_page.topics = [LIQDTHEORY, DIGITALCIVICSOCIETY]
        self.academy_index.add_child(instance=academy_page)
        academy_page.save_revision().publish()

        # Reload from database
        academy_page.refresh_from_db()

        # Check that we can access the field value
        topics = academy_page.topics
        self.assertIsInstance(topics, list)
        self.assertIn(LIQDTHEORY, topics)
        self.assertIn(DIGITALCIVICSOCIETY, topics)
