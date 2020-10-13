import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "apps.settings")
    import django
    django.setup()
    from app01 import models
    rel = models.Author.objects.all()
    print(rel.query)
