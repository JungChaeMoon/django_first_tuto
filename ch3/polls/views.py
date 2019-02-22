# -*- coding: utf-8 -*-
# Create your views here.
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from polls.models import Choice, Question
from django.views.generic.base import RedirectView
from django.views.generic import ListView,DetailView


class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(DetailView):  #특정 개체하나를 컨텍스트변수에 담아서 넘겨줌 근데 그변수가 pk로 조회하는경우 그냥 모델클래스만 지정해주면됨
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request,question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
             'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))



"""

def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]   #question 테이블 객체에서 질문이 생성된 역순으로다가 5개 설정
    context = {'latest_question_list': latest_question_list}  #templates에 사용될 변수명과 그변수명에 해당하는 객체를 매핑하는 사전으로 context 변수를 만들어서 이를render함수로 보냄
    return render(request, 'polls/index.html', context)  # render()함수는 템플릿 파일인 polls/index.html에 context 변수를 적용하여 사용자에게 보여줄 최종 html텍스트를 만들고 이를담아서  response객체에 반환

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #설문 투표 폼을 다시 보여준다
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

"""