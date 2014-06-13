from django.contrib import admin

# Register your models here.
from polls.models import Poll, Choice, Category

class ChoiceInline(admin.StackedInline):
 model = Choice
 extra = 3

class PollAdmin(admin.ModelAdmin):
 inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Category)
