# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin
from polls.models import Question, Choice

from django.contrib import admin
from polls.models import Question, Choice

#class ChoiceInline(admin.StackedInline):   #question fields 보여지는 형식 변경
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text']  컬럼 보여지는 순서 변경
    fieldsets = [
        ('Question Statement', {'fields':['question_text']}),
        #('Date Information', {'fields': ['pub_date']})
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']})  #숨김기능
    ]
    inlines = [ChoiceInline] #Choice 모델 클래스 같이보기
    list_display = ('question_text', 'pub_date') #레코드 리스트 컬럼 항목 지정
    list_filter = ['pub_date'] #필터사이드 바 추가
    search_fields = ['question_text']   # 검색박스 추가


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)