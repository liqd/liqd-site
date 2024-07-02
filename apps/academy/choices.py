from django.utils.translation import gettext_lazy as _

LIQDTHEORY = "LT"
DIGITALCIVICSOCIETY = "DS"
PARTICIPATIONACTION = "PA"

TOPIC_CHOICES = [
    (LIQDTHEORY, _("Liquid Democracy: Theory & Vision")),
    (DIGITALCIVICSOCIETY, _("Digital Civic Society")),
    (PARTICIPATIONACTION, _("Digital Participation In Action")),
]
