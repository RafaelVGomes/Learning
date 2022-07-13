from django.shortcuts import render
from django.http import HttpResponse as res

def index(req):
  return res("Hello, world. You're at the polls index.")

