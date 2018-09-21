from django.contrib import admin

from .models import *

admin.site.register(CompanyProfile)
admin.site.register(LeavePage)



class DisplayFeedback(admin.ModelAdmin):
	list_display =('Name','Email','Phone','Subject','Message')
	search_fields =['Name','Subject']
	list_filter =('Name','Subject','Email')
admin.site.register(Feedback,DisplayFeedback)
