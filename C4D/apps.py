from django.apps import AppConfig
from django.db.models.signals import post_migrate

def add_view_permissions(sender, **kwargs):
    """
    This hooks takes care of adding a view permission too all our content types.
    """
    from django.contrib.contenttypes.models import ContentType
    from django.contrib.auth.models import Group, Permission

    # Add or get our readonly group
    readonly_group, created = Group.objects.get_or_create(name='readonly')
    if created:
        print ("Added readonly Group")

    ignored_content_types = ['log entry' 'permission', 'group', 'user', 'content type', 'session']
    for ct in ContentType.objects.all():
        if not str(ct) in ignored_content_types:
            codename = "view_%s" % ct.model
            if not Permission.objects.filter(content_type=ct, codename=codename):
                p = Permission.objects.create(content_type=ct, codename=codename, name="Can view %s" % ct.name)
                print("Added view permission for %s" % ct.name)
                readonly_group.permissions.add(p)

class C4DAppConfig(AppConfig):
    name = "C4D"
    def ready(self):
        post_migrate.connect(add_view_permissions, sender=self)
