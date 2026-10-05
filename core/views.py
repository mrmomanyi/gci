from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import JourneyEntry


def home(request):
    latest = JourneyEntry.objects.filter(published=True)[:3]
    return render(request, "core/home.html", {"latest": latest})


def about(request):
    return render(request, "core/about.html")


def journey(request):
    entries = JourneyEntry.objects.filter(published=True)
    return render(request, "core/journey.html", {"entries": entries})


def journey_detail(request, slug):
    entry = get_object_or_404(JourneyEntry, slug=slug, published=True)
    return render(request, "core/journey_detail.html", {"entry": entry})


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        msg = form.save()
        if settings.CONTACT_EMAIL:
            send_mail(
                subject=f"New message on the GCI website from {msg.name}",
                message=f"{msg.message}\n\nReply to: {msg.email}",
                from_email=None,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=True,
            )
        return redirect("contact_thanks")
    return render(request, "core/contact.html", {"form": form})


def contact_thanks(request):
    return render(request, "core/contact_thanks.html")
