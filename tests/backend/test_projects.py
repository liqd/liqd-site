from django.test import TestCase
from wagtail.models import Page

from apps.core.models.snippets import ProjectCategory
from apps.projects.models import ProjectIndexPage
from apps.projects.models import ProjectPage


class ProjectPageOtherProjectTestCase(TestCase):
    """Regression tests for other_project on revision objects."""

    def setUp(self):
        root_page = Page.objects.filter(depth=1).first()
        self.category = ProjectCategory.objects.create(name_en="Test category")

        self.index = ProjectIndexPage(title="Projects", slug="projects")
        root_page.add_child(instance=self.index)

        self.project = ProjectPage(title="Project", slug="project")
        self.index.add_child(instance=self.project)
        self.project.categories.set([self.category])
        self.project.save_revision().publish()

        self.other = ProjectPage(title="Other project", slug="other-project")
        self.index.add_child(instance=self.other)
        self.other.categories.set([self.category])
        self.other.save_revision().publish()

    def test_other_project_on_revision_object(self):
        # Preview renders the page from a revision, where modelcluster
        # provides a FakeQuerySet for categories.
        revision_object = self.project.latest_revision.as_object()

        other_project = revision_object.other_project

        self.assertIsInstance(other_project, ProjectPage)
        self.assertNotEqual(other_project.pk, self.project.pk)

    def test_other_project_without_categories_on_revision_object(self):
        page = ProjectPage(title="Without category", slug="without-category")
        self.index.add_child(instance=page)
        page.save_revision().publish()

        revision_object = page.latest_revision.as_object()

        self.assertIsNone(revision_object.other_project)
