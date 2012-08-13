"""
Basic behind-the-scenes maintenance for superusers,
via django.contrib.admin.
"""

import models
from django.contrib import admin

class SubmittedThingAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_datetime'
    model = models.SubmittedThing
    list_display = ('id', 'created_datetime', 'updated_datetime', 'submitter_name',)

class DataSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'short_name', 'display_name')
    prepopulated_fields = {'short_name': ['display_name']}

class PlaceAdmin(SubmittedThingAdmin):
    model = models.Place

class SubmissionSetAdmin(admin.ModelAdmin):
    list_display = ('id', 'submission_type',)
    list_filter = ('submission_type',)

class SubmissionAdmin(SubmittedThingAdmin):
    model = models.Submission

class ActivityAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_datetime'
    list_display = ('id', 'created_datetime', 'action', 'submitter_name')

admin.site.register(models.DataSet, DataSetAdmin)
admin.site.register(models.Place, PlaceAdmin)
admin.site.register(models.SubmissionSet, SubmissionSetAdmin)
admin.site.register(models.Submission, SubmissionAdmin)
admin.site.register(models.Activity, ActivityAdmin)
