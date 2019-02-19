# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from polls.models import Question, Choice

from django.contrib import admin
from polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Statement', {'fields':['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)