from django.contrib import admin
from .models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'isim', 'user', 'slug')
    list_display_links = ('id', 'user')
    search_fields = ('isim',)
    list_editable = ('isim',)
    list_per_page = 4
    list_filter = ('isim', 'user')
    readonly_fields = ('slug',)
    
# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Account)