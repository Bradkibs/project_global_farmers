from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import uuid
from product_api.models import Product
from auth_api.models import User


class InspectorProductRelation(models.Model):
    class GradeChoices(models.TextChoices):
        A = 'A', _('A')
        B = 'B', _('B')
        C = 'C', _('C')

    class StatusChoices(models.TextChoices):
        INSPECTED = 'INSPECTED', _('inspected')
        REJECTED = 'REJECTED', _('rejected')
        PENDING = 'PENDING', _('pending')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    inspector = models.ForeignKey(User, on_delete=models.CASCADE)
    product_inspected = models.ForeignKey(Product, on_delete=models.CASCADE)
    comments = models.CharField(max_length=320, default='')
    status = models.CharField(max_length=20,
                              choices=StatusChoices.choices,
                              default=StatusChoices.PENDING
                              )
    grade = models.CharField(max_length=2, choices=GradeChoices.choices)
    restriction = models.TextChoices('restricted', 'approved')
    reviewed_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f'{self.inspector.full_name}'

    class Meta:
        verbose_name = _('inspector_product_relation_table')


