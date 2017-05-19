from django.contrib import admin

from . import models


class ChoicesAdmin(admin.ModelAdmin):
    list_display = ('field', 'value')
    list_filter = ('field',)


class ChoicesInline(admin.StackedInline):
    model = models.FieldChoice


class FieldAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'required', 'order')
    inlines = [ChoicesInline]


admin.site.register(models.FieldChoice, ChoicesAdmin)
admin.site.register(models.Field, FieldAdmin)
