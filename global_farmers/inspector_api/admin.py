from django.contrib import admin
from .models import InspectorProductRelation
from django.core.exceptions import PermissionDenied


class InspectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'inspector', 'product_inspected', 'comments', 'status', 'grade', 'restriction', 'reviewed_at')

    def has_add_permission(self, request):
        return not hasattr(request.user, 'user_type') and request.user.user_type == 'INSPECTOR'

    def has_change_permission(self, request, obj=None):
        return request.user.user_type == 'INSPECTOR'

    def add_view(self, request, form_url='', extra_context=None):
        if not self.has_add_permission(request):
            raise PermissionDenied('You can not add products from a user that is not an Inspector!')
        return super().add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if not self.has_change_permission(request, obj):
            raise PermissionDenied('You can not change products from a user that is not an Inspector!')
        return super().change_view(request, object_id, form_url, extra_context)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

    readonly_fields = ('inspector', 'reviewed_at',)


admin.site.register(InspectorProductRelation, InspectorAdmin)

