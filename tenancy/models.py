from django.db import models
from middleware import get_current_user


class TenantManager(models.Manager):

    def get_queryset(self):
        if not (get_current_user() is None or get_current_user().is_anonymous()):
            return super(TenantManager, self).get_queryset().filter(organization=get_current_user().organization)
        return super(TenantManager, self).get_queryset()


class TenantAware(models.Model):
    tenant_objects = TenantManager()
    objects = models.Manager()
    class Meta:
        abstract = True
