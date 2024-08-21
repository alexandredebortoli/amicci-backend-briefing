from django.contrib import admin

from briefing_api.models import Briefing, Category, Retailer, Vendor

admin.site.register(Vendor)
admin.site.register(Retailer)
admin.site.register(Category)
admin.site.register(Briefing)
