# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from polls.models import Question, Choice

from django.contrib import admin
from polls.models import Question, Choice


admin.site.register(Question)
admin.site.register(Choice)