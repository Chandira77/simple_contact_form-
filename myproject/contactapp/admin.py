from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at']
    #list_filter = ['status']
    search_fields = ['name', 'email', 'message']

admin.site.register(Contact, ContactAdmin)
