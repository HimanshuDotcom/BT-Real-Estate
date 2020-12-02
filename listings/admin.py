from django.contrib import admin
from .models import listing

class listingAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'price')
    list_per_page = 25
# Register your models here.
admin.site.register(listing, listingAdmin)
