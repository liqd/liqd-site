from .abstract_page_model import TranslatedStreamFieldPage


class HomePage(TranslatedStreamFieldPage):
    subpage_types = [
        "TextPageWithBlocks",
        "TextPage",
        "projects.ProjectIndexPage",
        "blog.BlogIndexPage",
        "academy.AcademyIndexPage",
        "academy.AcademyChallengePage",
        "academy.AcademyLandingPage",
    ]
