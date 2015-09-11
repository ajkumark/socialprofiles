from django.contrib import admin
from fullcontactapp.models import *

class ContactAdmin(admin.ModelAdmin):
	list_display = ('email', 'created')

class NotFoundContactAdmin(admin.ModelAdmin):
	list_display = ('email', 'created')

class AprilFoolAdmin(admin.ModelAdmin):
	list_display = ('phone', 'created')

admin.site.register(Contact, ContactAdmin)
admin.site.register(FullContact)
admin.site.register(NotFoundContact,NotFoundContactAdmin)
admin.site.register(AprilFool,AprilFoolAdmin)