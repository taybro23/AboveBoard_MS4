from django.db import models


class HelpGuidance(models.Model):

    class Meta:
        verbose_name_plural = 'Help & Guidance'

    title = models.CharField(max_length=254, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return str(self.title)
