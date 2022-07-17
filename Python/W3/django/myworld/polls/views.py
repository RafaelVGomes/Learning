from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.http import HttpResponse as res, HttpResponseRedirect as red
from django.urls import reverse
from django.views import generic

from .models import Question, Choice

def index(req):
  latest_question_list = Question.objects.order_by('-pub_date')
  context = {
    'latest_question_list': latest_question_list
  }
  return render(req, 'polls/index.html',context)

def detail(req, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(req, 'polls/detail.html', {'question': question})

def results(req, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(req, 'polls/results.html', {'question': question})

def vote(req, question_id):
  question = get_object_or_404(Question, pk=question_id)
  try:
    selected_choice = question.choice_set.get(pk=req.POST['choice'])
    selected_choice.refresh_from_db()
  except (KeyError, Choice.DoesNotExist):
    return render(req, 'polls/detail.html', {
      'question': question,
      'error_message': "You didn't select a choice."
    })
  else:
    selected_choice.votes = F('votes') + 1
    selected_choice.save()
  return red(reverse('polls:results', args=(question.id,)))