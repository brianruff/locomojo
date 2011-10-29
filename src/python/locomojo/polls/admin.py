from polls.models import Poll
from django.contrib import admin
from polls.models import Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

#re-order admin form fields
class PollAdmin(admin.ModelAdmin):

   list_filter = ['pub_date']
   search_fields = ['question']
   date_hierarchy = 'pub_date'

   fieldsets = [
       (None, {'fields': ['question']}),
       ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),

   ]


inlines = [ChoiceInLine]
list_display = ('question', 'pub_date', 'was_published_today')


admin.site.register(Poll, PollAdmin)

