from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class PollAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question','poll_user']}),
    #     ('Date information', {'fields': ['pub_date','created','updated'], 'classes': ['collapse']}),
    # ]
    inlines = [ChoiceInline]
    list_display = ('question', 'pub_date','was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)