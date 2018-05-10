from django.contrib import admin
from .models import Heroes
from django.contrib.admin.templatetags.admin_list import admin_list_filter
# Register your models here.

class HeroModelAdmin(admin.ModelAdmin):
    list_display = ["hero", "update", "timestamp"]
    list_display_links = ["hero"]
    list_filter = ["hero", "update", "timestamp"]
    search_fields = ["hero", "info", "update", "timestamp"]
    #list_editable =  ["hero"]
    class Meta:
        model = Heroes



admin.site.register(Heroes, HeroModelAdmin)