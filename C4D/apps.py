from django.apps import AppConfig
from django.db.models.signals import post_migrate

def add_view_permissions(sender, **kwargs):
    """
    This hooks takes care of adding a view permission too all our content types.
    """
    from django.contrib.contenttypes.models import ContentType
    from django.contrib.auth.models import Permission
    for content_type in ContentType.objects.all():
        codename = "view_%s" % content_type.model
        if not Permission.objects.filter(content_type=content_type, codename=codename):
            Permission.objects.create(content_type=content_type,
                                      codename=codename,
                                      name="Can view %s" % content_type.name)
            print("Added view permission for %s" % content_type.name)


class C4DAppConfig(AppConfig):
    name = "C4D"
    def ready(self):
        post_migrate.connect(add_view_permissions, sender=self)
