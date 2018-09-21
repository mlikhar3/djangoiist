from django.contrib import admin
from django import forms

# Register your models here.
from .models import *

# def complete_tasks(modeladmin, request, queryset):
#     queryset.update(completed=True)
# complete_tasks.short_description = 'Mark as Complete'

def send_email(self, request, queryset):
    from django.core.mail import send_mail
    for i in queryset:
        if i.email:
            send_mail('Subject here', 'Here is the message.', 'mansi.deolalikar@gmail.com',[i.email], fail_silently=False)
        else:
        	self.message_user(request, "Mail sent successfully ") 
        #message.add_message(request, message.INFO, 'Feedback Submitted')
send_email.short_description = "Send an email to selected users"

# def send_email(self, request, queryset):
#     from django.core.mail import send_mail
#     for i in queryset:
#         if i.email:
#             form = SendEmailForm(initial={'user': queryset})
#             return render(request, 'authentication/send_email.html', {'form': form})
#         else:
#             self.message_user(request, "Mail sent successfully ") 
#     send_email.short_description = "Send an email to selected users"

# class SendEmailForm(forms.Form):
#     subject = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': ('Subject')}))
#     message = forms.CharField(widget=forms.Textarea)
#     user = forms.ModelMultipleChoiceField(label="To",
#                                            queryset=User.objects.all(),
#                                            widget=forms.SelectMultiple())


    
class DisplayProfile(admin.ModelAdmin):
    list_display =('first_name','email','phone','branch')
    search_fields =['first_name','branch']
    list_filter =('cgpa','branch','ten','twelve')
    actions = [send_email]


admin.site.register(Profile,DisplayProfile)