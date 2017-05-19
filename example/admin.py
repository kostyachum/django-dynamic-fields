from django.contrib import admin
from . import models


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'address')
    search_fields = ('user__username', 'address')
    readonly_fields = ('custom_field_data',)


admin.site.register(models.Customer, CustomerAdmin)
