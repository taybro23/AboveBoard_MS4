from django.contrib import admin
from .models import HelpGuidance


class HelpAdmin():
    list_display = (
        'title',
        'body',
        'image',
    )


admin.site.register(HelpGuidance)
