# Fun Django Site with Allauth, SAML, and CAS

This is a simple Django project with:
- [django-allauth](https://github.com/pennersr/django-allauth) for authentication
- SAML and CAS login integration
- A fun, green-on-black themed main page

## Quick Start

1. **Install dependencies** (already done if you followed setup):
   ```zsh
   python3 -m venv .venv
   source .venv/bin/activate
   pip install django django-allauth djangosaml2 django-cas-ng
   ```
2. **Run migrations:**
   ```zsh
   python manage.py migrate
   ```
3. **Run the server:**
   ```zsh
   python manage.py runserver
   ```
4. Visit [http://localhost:8000/](http://localhost:8000/) to see the main page.

## Authentication
- Login with Allauth: `/accounts/login/`
- Login with SAML: `/saml2/login/`
- Login with CAS: `/cas/login/`

## Customization
- Main page template: `main/templates/main/home.html`
- Main page CSS: `main/static/main/style.css`

---
This project is for demo purposes. Fill in SAML and CAS config in `settings.py` for real integrations.
