from django.db import models
from django.urls import reverse
from django.utils import timezone


class JourneyEntry(models.Model):
    """One milestone, update or story in the GCI journey."""

    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    date = models.DateField(default=timezone.localdate, help_text="When this happened.")
    summary = models.CharField(max_length=280, help_text="One or two sentences shown in lists.")
    body = models.TextField(blank=True, help_text="Full story. Blank lines start a new paragraph.")
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "-created"]
        verbose_name_plural = "journey entries"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("journey_detail", kwargs={"slug": self.slug})


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    handled = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} ({self.created:%Y-%m-%d})"
