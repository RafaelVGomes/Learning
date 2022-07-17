from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
  path('', views.index.as_view(), name='index'),
  path('<int:pk>/', views.detail.as_view(), name='detail'),
  path('<int:pk>/results/', views.results.as_view(), name='results'),
  path('<int:question_id>/vote/', views.vote.as_view(), name='vote'),
]