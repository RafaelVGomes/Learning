from django.db.models import F
from django.http import HttpResponse as res
from django.http import HttpResponseRedirect as red
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
  template_name = 'polls/index.html'
  context_object_name = 'latest_question_list'

  def get_queryset(self):
    return Question.objects.order_by('-pub_date')
  

class DetailView(generic.DetailView):
  model = Question
  template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
  model = Question
  template_name = 'polls/results.html'

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
