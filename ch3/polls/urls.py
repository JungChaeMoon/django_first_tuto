from django.urls import path
from . import views

app_name = 'polls'

urlpatterns=[
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


"""
question_id i는 models  에서 declare 되었는데 why안넘어갈까
"""