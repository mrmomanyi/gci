# Global Climate Innovators website

A small Django site: Home, About, Our journey (a timeline you edit in the admin), and Contact.

## Run it locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations core
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ for the site and http://127.0.0.1:8000/admin/ to manage it.

## Day-to-day use

- **Add a milestone:** Admin > Journey entries > Add. Untick "published" to keep a draft.
- **Read messages:** Admin > Contact messages. Set `GCI_CONTACT_EMAIL` to also get each message by email.
- **Edit page text:** About and Home copy lives in `core/templates/core/`. The About page text is placeholder: replace it with your own story.
- **Change name, tagline or colors:** `config/settings.py` (SITE_NAME, SITE_TAGLINE) and `core/static/core/css/site.css` (the variables at the top).
- **Logo:** the mark is an inline SVG in `core/templates/core/partials/mark.html`.

## Before going live

Set these environment variables on your host:

```
DJANGO_SECRET_KEY=<a long random string>
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=yourdomain.org,www.yourdomain.org
DJANGO_CSRF_TRUSTED_ORIGINS=https://yourdomain.org,https://www.yourdomain.org
GCI_CONTACT_EMAIL=you@yourdomain.org
```

Then run `python manage.py collectstatic --noinput` and serve with `gunicorn config.wsgi`.
For email delivery, set `DJANGO_EMAIL_BACKEND` and the standard Django SMTP settings.
