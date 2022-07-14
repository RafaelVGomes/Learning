from django.shortcuts import render
from django.http import HttpResponse as res

from .models import Question

def index(req):
  latest_question_list = Question.objects.order_by('-pub_date')[:5]
  output = ', '.join([q.question_text for q in latest_question_list])
  return res(output)

def detail(req, question_id):
  return res(f"You're looking at question: {question_id}")

def results(req, question_id):
  return res(f"You're looking at the results of: {question_id}")

def vote(req, question_id):
  return res(f"You're voting on question: {question_id}")